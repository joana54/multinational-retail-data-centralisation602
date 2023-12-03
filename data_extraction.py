import pandas as pd
from tabula.io import read_pdf
import requests
import boto3
from data_cleaning import DataCleaning

STORES_ENDPOINT = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
RETRIEVAL_ENDPOINT = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details"
HEADERS = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
PRODUCT_DATA_ADDRESS = "s3://data-handling-public/products.csv"

class DataExtractor:
    def read_rds_table(table_name, engine):
        df = pd.read_sql_table(table_name, engine)
        return df
    

    def retrieve_pdf_data(pdf_path):
        df_list = read_pdf(pdf_path, stream=False, pages="all")
        card_data = pd.concat(df_list, ignore_index=True)
        return card_data
    

    def list_number_of_stores(stores_endpoint, headers):
        response = requests.get(stores_endpoint, headers=headers)
        return response.json()["number_stores"]


    def retrieve_stores_data(retrieval_endpoint, headers):
        number_of_stores = DataExtractor.list_number_of_stores(STORES_ENDPOINT, headers)
        store_data_frames = []
        for store_number in range(number_of_stores):
            response = requests.get(f"{retrieval_endpoint}/{store_number}", headers=headers)
            store_data_frames.append(response.json())
        return pd.DataFrame(store_data_frames)
    

    def extract_from_s3(data_address):
        split_address = data_address.split("/")
        bucket_name = split_address[2]
        file_name = split_address[3]

        s3_client = boto3.client("s3")
        s3_client.download_file(bucket_name, file_name, "products_data.csv")