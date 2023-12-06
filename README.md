# Multinational Retail Data Centralisation

A project to collate the sales data of a multinational retail company from multiple data sources and combine them into one database for simpler analysis. Data is extracted using methods from the data_extraction.py file and then cleaned using methods from the data_cleaning.py file. The database_utils.py file contains methods used to connect to a postgres databse, supporting both a local connection and a connection to an AWS RDS database. The configuaration for these connections must be contained in a yaml file, the setup of which is detailed below. The main.py file will extract data from all the various data sources, clean it and finally upload the data to a local postgres database by default. This can be changed by altering what yaml file is being read. The table_conversion.sql file converts data types of the tables created and adds primary key and foreign key constraints to the tables. Finally, the sql_queries.sql file containes the queries needed to extract data that provides up-to-date metrics.

## Installation

Install git for your system from here:

https://git-scm.com/downloads

Install python for your system here:

https://www.python.org/downloads/

Use git to clone the repo by running the command in your terminal or command prompt:

git clone https://github.com/joana54/multinational-retail-data-centralisation602.git

Navigate to the repository in your terminal or command prompt and install dependecies by running the following command:

pip install -r requirements.txt

## Usage

Run the project by running the following command in your terminal or command prompt:

python main.py

## YAML File Configuration

RDS_HOST: {hostname of database}

RDS_PASSWORD: {password for database}

RDS_USER: {username of user trying to access database}

RDS_DATABASE: {name of database to connect to}

RDS_PORT: {port of database}