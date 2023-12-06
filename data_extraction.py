import boto3
import pandas as pd
import requests
from data_cleaning import DataCleaning
from tabula.io import read_pdf


STORES_ENDPOINT = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
RETRIEVAL_ENDPOINT = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details"
HEADERS = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
PRODUCT_DATA_ADDRESS = "s3://data-handling-public/products.csv"
DATE_DETAILS_ADDRESS = "s3://data-handling-public/date_details.json"


class DataExtractor:
    
    def read_rds_table(table_name, engine):
        """This function takes in a table name and engine object and return a DataFrame. """
        df = pd.read_sql_table(table_name, engine)
        return df
    
    def retrieve_pdf_data(pdf_path):
        """This function takes in the link of the PDF file,concatenates the series 
        from the PDF file and returns a DataFrame"""
        df_list = read_pdf(pdf_path, stream=False, pages="all")
        card_data = pd.concat(df_list, ignore_index=True)
        return card_data
    
    def list_number_of_stores(stores_endpoint, headers):
        """This function takes in the number of stores endpoint and header dictionary as an 
        argument and returns the number of stores. """
        response = requests.get(stores_endpoint, headers=headers)
        return response.json()["number_stores"]

    def retrieve_stores_data(retrieval_endpoint, headers):
        """This function takes the retrieve a store endpoint and headers as an argument, extracts all the 
        stores and saves them in a DataFrame."""
        number_of_stores = DataExtractor.list_number_of_stores(STORES_ENDPOINT, headers)
        store_data_frames = []
        for store_number in range(number_of_stores):
            response = requests.get(f"{retrieval_endpoint}/{store_number}", headers=headers)
            store_data_frames.append(response.json())
        return pd.DataFrame(store_data_frames)
    
    def extract_from_s3(data_address, local_filename):
        """This function takes the address to the bucket and name of the file the downloaded data is saved as."""
        split_address = data_address.split("/")
        bucket_name = split_address[2]
        filename = split_address[3]

        s3_client = boto3.client("s3")
        s3_client.download_file(bucket_name, filename, local_filename)