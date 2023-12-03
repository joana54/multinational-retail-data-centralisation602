import pandas as pd
import numpy as np


class DataCleaning:

    def clean_user_data(users_df):
     
        users_df.date_of_birth = pd.to_datetime(users_df.date_of_birth, format="mixed", errors="coerce")
        users_df.join_date = pd.to_datetime(users_df.join_date, format="mixed", errors="coerce")
        str_columns = ["first_name", "last_name", "company",
                       "email_address", "address", "country", 
                       "country_code", "phone_number", "user_uuid"]
        
        users_df[str_columns] = users_df[str_columns].astype("string")
    

        users_df = users_df.replace("NULL", np.nan)
        users_df = users_df.dropna()
        users_df.reset_index(drop=True, inplace=True)

        users_df["country_code"] = users_df["country_code"].replace("GGB", "GB")

        return users_df
    
    def clean_card_data(card_data_df):
        card_data_df = card_data_df.replace("NULL", np.nan)
        card_data_df.expiry_date = pd.to_datetime(card_data_df.expiry_date, format="mixed", errors="coerce")
        card_data_df.date_payment_confirmed = pd.to_datetime(card_data_df.date_payment_confirmed, format="mixed", errors="coerce")
        card_data_df = card_data_df.dropna()
        card_data_df["card_number"] = card_data_df["card_number"].astype(int)
        return card_data_df
    
    def clean_store_data(store_df):
        store_df = pd.read_csv("data/stores_data.csv")
        store_df = store_df.drop("lat", axis=1)
        store_df.opening_date = pd.to_datetime(store_df.opening_date, format="mixed", errors="coerce")
        store_df = store_df[~store_df['opening_date'].isnull()]
        store_df["address"] = store_df["address"].replace("\n", ", ", regex=True)
        store_df[["latitude", "longitude"]] = store_df[["latitude", "longitude"]].astype(float)
        return store_df

    def convert_product_weights(weight):
        if "kg" in weight:
            weight = weight.replace("kg", "")
            weight = np.format_float_positional(float(weight), precision=3)
            return weight
        
        if "x" in weight:
            weight_multiplication_numbers = weight.split(" x ")
            base_weight = weight_multiplication_numbers[1]
            multiplier = int(weight_multiplication_numbers[0])

            base_weight = base_weight.replace("g", "")
            base_weight = float(base_weight)
            total_weight = weight = np.format_float_positional((multiplier * base_weight), precision=3)

            return total_weight
        
        if "g" in weight:

            if "." in weight:
                if len(weight.split(".")[0]) == 1:
                    weight = weight.replace("g", "")
                    weight = np.format_float_positional(float(weight), precision=3)
                    return weight
        
            weight = weight.replace(weight[weight.index("g"):], "")
            weight = np.format_float_positional((float(weight)/1000), precision=3)
            return weight
        
        if "ml" in weight:
            weight = weight.replace("ml", "")
            weight = np.format_float_positional((float(weight)/1000), precision=3)
            return weight
        
    def clean_products_data(filename):
        products_df = pd.read_csv(filename)
        products_df = products_df.rename(columns={"Unnamed: 0": "index"})
        products_df.date_added = pd.to_datetime(products_df.date_added, format="mixed", errors="coerce")
        products_df = products_df[~products_df['date_added'].isnull()]
        products_df["weight"] = products_df["weight"].apply(DataCleaning.convert_product_weights)
        products_df["product_price"] = products_df["product_price"].replace("£", "", regex=True)
        return products_df
    
    def clean_orders_data(orders_df):
        orders_df = orders_df.drop(columns=["level_0", "1", "first_name", "last_name"])
        return orders_df
    
    def clean_date_details_data(filename):
        date_details_df = pd.read_json(filename)

        date_details_df = date_details_df.drop_duplicates()

        date_details_df["date"] = pd.to_datetime(date_details_df[["year", "month", "day"]], errors="coerce").astype(str)
        date_details_df["datetime"] = date_details_df["date"] + " " + date_details_df["timestamp"]
        date_details_df["datetime"] = pd.to_datetime(date_details_df["datetime"], format="mixed", errors="coerce")

        date_details_df = date_details_df.drop(columns=["timestamp", "month", "year", "day", "date"])

        date_details_df = date_details_df.dropna()

        return date_details_df


