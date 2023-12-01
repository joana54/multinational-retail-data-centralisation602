import pandas as pd
from database_utils import DatabaseConnector

class DataExtractor:
    def read_rds_table(table_name, engine):
        df = pd.read_sql_table(table_name, engine)
        return df