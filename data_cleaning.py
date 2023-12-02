import pandas as pd
import numpy as np


class DataCleaning:
    def clean_user_data(users_df):
     
        users_df.date_of_birth = pd.to_datetime(users_df.date_of_birth, format='mixed', errors='coerce')
        users_df.join_date = pd.to_datetime(users_df.join_date, format='mixed', errors='coerce')
        str_columns = ['first_name', 'last_name', 'company',
                       'email_address', 'address', 'country', 
                       'country_code', 'phone_number', 'user_uuid']
        
        users_df[str_columns] = users_df[str_columns].astype('string')
    

        users_df = users_df.replace('NULL', np.nan)
        users_df = users_df.dropna()
        users_df.reset_index(drop=True, inplace=True)

        users_df['country_code'] = users_df['country_code'].replace('GGB', 'GB')

        return users_df
    

    def clean_card_data(card_data_df):
        card_data_df = card_data_df.replace('NULL', np.nan)
        card_data_df.expiry_date = pd.to_datetime(card_data_df.expiry_date, format='mixed', errors='coerce')
        card_data_df.date_payment_confirmed = pd.to_datetime(card_data_df.date_payment_confirmed, format='mixed', errors='coerce')
        card_data_df = card_data_df.dropna()
        return card_data_df


