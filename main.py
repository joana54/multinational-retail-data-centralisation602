from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

rds_connector = DatabaseConnector("db_creds.yaml")
rds_engine = rds_connector.init_db_engine()
legacy_users_df = DataExtractor.read_rds_table("legacy_users", rds_engine)
cleaned_users_df = DataCleaning.clean_user_data(legacy_users_df)
local_connector = DatabaseConnector("local_sql_database.yaml")
local_connector.upload_to_db("dim_users", cleaned_users_df)

pdf_path = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
card_data_df = DataExtractor.retrieve_pdf_data(pdf_path)
cleaned_card_df = DataCleaning.clean_card_data(card_data_df)
local_connector.upload_to_db("dim_card_details", cleaned_card_df)