import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect

class DatabaseConnector:

    def __init__(self, yaml_file) -> None:
        self.yaml_file = yaml_file
        

    def read_db_creds(self):
        with open(self.yaml_file, "r") as f:
            creds  = yaml.safe_load(f)
            return creds


    def init_db_engine(self):
        credentials = self.read_db_creds()
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
        return engine
        

    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        print(inspector.get_table_names())

    
    def upload_to_db(self, table_name, df):
        connection = self.init_db_engine()
        df.to_sql(table_name, connection, index=False, if_exists='replace')
