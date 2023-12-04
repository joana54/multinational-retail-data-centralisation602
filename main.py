from database_utils import DatabaseConnector
from data_extraction import DataExtractor, RETRIEVAL_ENDPOINT, HEADERS, PRODUCT_DATA_ADDRESS, DATE_DETAILS_ADDRESS
from data_cleaning import DataCleaning
import sqlalchemy
import pandas as pd
PDF_PATH = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
LOCAL_YAML = "local_sql_database.yaml"
RDS_YAML = "db_creds.yaml"

# rds_connector = DatabaseConnector(RDS_YAML)
# rds_engine = rds_connector.init_db_engine()
# legacy_users_df = DataExtractor.read_rds_table("legacy_users", rds_engine)
# cleaned_users_df = DataCleaning.clean_user_data(legacy_users_df)
local_connector = DatabaseConnector(LOCAL_YAML)
local_engine = local_connector.init_db_engine()
# local_connector.upload_to_db("dim_users", cleaned_users_df)

# card_data_df = DataExtractor.retrieve_pdf_data(PDF_PATH)
# cleaned_card_df = DataCleaning.clean_card_data(card_data_df)
# local_connector.upload_to_db("dim_card_details", cleaned_card_df)

# store_df = DataExtractor.retrieve_stores_data(RETRIEVAL_ENDPOINT, HEADERS)
# cleaned_store_df = DataCleaning.clean_store_data(store_df)
# local_connector.upload_to_db("dim_store_details", cleaned_store_df)

# DataExtractor.extract_from_s3(PRODUCT_DATA_ADDRESS, "products_data.csv")
# cleaned_products_df = DataCleaning.clean_products_data("products_data.csv")
# local_connector.upload_to_db("dim_products", cleaned_products_df)

# orders_df = DataExtractor.read_rds_table("orders_table", rds_engine)
# cleaned_orders_df = DataCleaning.clean_orders_data(orders_df)
# local_connector.upload_to_db("orders_table", cleaned_orders_df)

# DataExtractor.extract_from_s3(DATE_DETAILS_ADDRESS, "date_details.json")
# cleaned_date_details_df = DataCleaning.clean_date_details_data("date_details.json")
# local_connector.upload_to_db("dim_date_times", cleaned_date_details_df)

with local_engine.connect() as con:
    with open("table_conversion.sql") as file:
        query = sqlalchemy.text(file.read())
        con.execute(query)
        con.commit()