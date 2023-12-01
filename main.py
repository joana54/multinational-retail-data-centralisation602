from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

rds_connector = DatabaseConnector("db_creds.yaml")
rds_engine = rds_connector.init_db_engine()
legacy_users_df = DataExtractor.read_rds_table("legacy_users", rds_engine)
cleaned_users_df = DataCleaning.clean_user_data(legacy_users_df)
local_connector = DatabaseConnector("local_sql_database.yaml")
local_connector.upload_to_db("dim_users", cleaned_users_df)