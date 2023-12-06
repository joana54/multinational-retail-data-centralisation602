import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect


class DatabaseConnector:

    def __init__(self, yaml_file) -> None:
        self.yaml_file = yaml_file
        
    def read_db_creds(self):
        """This function loads a yaml file and returns it."""
        with open(self.yaml_file, "r") as f:
            creds  = yaml.safe_load(f)
            return creds

    def init_db_engine(self):
        """This function creates a connection to a database and returns an engine object."""
        credentials = self.read_db_creds()
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
        return engine
        
    def list_db_tables(self):
        """This function connects to a database and prints the names of the tables contained within it. """
        engine = self.init_db_engine()
        inspector = inspect(engine)
        print(inspector.get_table_names())

    def upload_to_db(self, table_name, df):
        """This function creates a connection to a database and uploads a DataFrame to the database. """
        connection = self.init_db_engine()
        df.to_sql(table_name, connection, index=False, if_exists='replace')
