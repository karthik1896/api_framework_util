"""
Module defines the SQLAlchemy model for storing environment details.
"""
from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configurations.config import connection_string

Base = declarative_base()


class Environment(Base):
    """
    SQLAlchemy model for storing environment details.

    This class represents the structure of the env_tbl table in the database.
    It defines various columns to store different attributes of environment data.

    Attributes:
        id (int): The unique identifier for each environment entry.
        env (str): The name of the environment.
        internal_url (str): The internal URL for the environment.
        gateway (str): The gateway URL for the environment.
        application (str): The application associated with the environment.
        username (str): The username for accessing the environment.
        password (str): The password for accessing the environment.
        login_url (str): The URL for logging into the environment.
        client_code (str): The client code associated with the environment.
        client_secret (str): The client secret associated with the environment.
        signing_key (str): The signing key used in the environment.
        encryption_type (str): The encryption type used in the environment.
        encryption_algorithm (str): The encryption algorithm used in the environment.
        login_cred (str): The login credentials for accessing the environment.
        client_type (str): The client type associated with the environment.
        login_type (str): The type of login used in the environment.
    """

    __tablename__ = "env_tbl"

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    env = Column("ENV", VARCHAR)
    internal_url = Column("INTERNAL_URL", VARCHAR)
    gateway = Column("GATEWAY_URL", VARCHAR)
    application = Column("APPLICATION", VARCHAR)
    username = Column("USERNAME", VARCHAR)
    password = Column("PASSWORD", VARCHAR)
    login_url = Column("LOGIN_URL", VARCHAR)
    client_code = Column("client_code", VARCHAR)
    client_secret = Column("client_secret", VARCHAR)
    signing_key = Column("signing_key", VARCHAR)
    encryption_type = Column("encryption_type", VARCHAR)
    encryption_algorithm = Column("encryption_algorithm", VARCHAR)
    login_cred = Column("login_cred", VARCHAR)
    client_type = Column("client_type", VARCHAR)
    login_type = Column("login_type", VARCHAR)


engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
