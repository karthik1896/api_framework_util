"""
Module defines the SQLAlchemy model for storing API configuration details.
"""
from sqlalchemy import create_engine, Column, Integer, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configurations.config import connection_string

Base = declarative_base()


class ApiConfiguration(Base):
    """
    Represents an API configuration entry in the database.

    Attributes:
        conf_id (int): The ID of the API configuration.
        application (str): The name of the application.
        module (str): The name of the module.
        sub_module (str): The name of the sub_module.
        api (str): The name of the API.
        port (int): The port number.
        internal_path (str): The internal path.
        gateway_path (str): The gateway path.
        db_details (str): The details of the database.
        success_schema (str): The success schema.
        internal_only (int): Flag indicating if the API is internal only.
    """

    __tablename__ = "api_configuration_mstr"

    conf_id = Column("CONF_ID", Integer, primary_key=True, autoincrement=True)
    application = Column("APPLICATION", VARCHAR, nullable=False)
    module = Column("MODULE", VARCHAR, nullable=False)
    sub_module = Column("SUB_MODULE", VARCHAR, nullable=False)
    api = Column("API", VARCHAR, nullable=False)
    port = Column("PORT", Integer, nullable=True)
    internal_path = Column("INTERNAL_PATH", VARCHAR, nullable=True)
    gateway_path = Column("GATEWAY_PATH", VARCHAR, nullable=True)
    db_details = Column("DB_DETAILS", VARCHAR, nullable=True)
    success_schema = Column("SUCCESS_SCHEMA", Text, nullable=True)
    internal_only = Column("INTERNAL_ONLY", Integer, nullable=True)


engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
