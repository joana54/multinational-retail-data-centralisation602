from database_utils import DatabaseConnector
from data_extraction import DataExtractor, RETRIEVAL_ENDPOINT, HEADERS, PRODUCT_DATA_ADDRESS
from data_cleaning import DataCleaning

PDF_PATH = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"

# rds_connector = DatabaseConnector("db_creds.yaml")
# rds_engine = rds_connector.init_db_engine()
# legacy_users_df = DataExtractor.read_rds_table("legacy_users", rds_engine)
# cleaned_users_df = DataCleaning.clean_user_data(legacy_users_df)
local_connector = DatabaseConnector("local_sql_database.yaml")
# local_connector.upload_to_db("dim_users", cleaned_users_df)

# card_data_df = DataExtractor.retrieve_pdf_data(PDF_PATH)
# cleaned_card_df = DataCleaning.clean_card_data(card_data_df)
# local_connector.upload_to_db("dim_card_details", cleaned_card_df)

# store_df = DataExtractor.retrieve_stores_data(RETRIEVAL_ENDPOINT, HEADERS)
# cleaned_store_df = DataCleaning.clean_store_data(store_df)
# local_connector.upload_to_db("dim_store_details", cleaned_store_df)

DataExtractor.extract_from_s3(PRODUCT_DATA_ADDRESS)
cleaned_products_df = DataCleaning.clean_products_data()
local_connector.upload_to_db("dim_products", cleaned_products_df)


