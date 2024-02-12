"""
Module to read configurations from conf.ini and construct connection strings.
"""
import urllib.parse
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read("configurations/conf.ini")

# Access values in the configuration file
database_host = config.get("MYSQL", "MYSQL_HOST")
database_port = config.getint("MYSQL", "MYSQL_PORT")
database_username = config.get("MYSQL", "MYSQL_USER")
database_password = config.get("MYSQL", "MYSQL_PASSWORD")
database_schema = config.get("MYSQL", "MYSQL_DATABASE")

escaped_password = urllib.parse.quote_plus(database_password)

# Construct the connection string
connection_string = f"mysql+mysqlconnector://{database_username}:{escaped_password}@{database_host}:{database_port}/{database_schema}"

api_port = int(config.get("UVICORN", "PORT"))
