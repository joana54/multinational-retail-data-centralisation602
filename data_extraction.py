import pandas as pd
from database_utils import DatabaseConnector
from tabula.io import read_pdf

class DataExtractor:
    def read_rds_table(table_name, engine):
        df = pd.read_sql_table(table_name, engine)
        return df
    

    def retrieve_pdf_data(pdf_path):
        df_list = read_pdf(pdf_path, stream=False, pages='all')
        card_data = pd.concat(df_list, ignore_index=True)
        return card_data
