"""
Module defines the SQLAlchemy model for storing TestData details.
"""
from sqlalchemy import Column, Integer, VARCHAR, JSON, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from configurations.config import connection_string

Base = declarative_base()


class TestData(Base):
    """
    SQLAlchemy model for storing TestData details.

    This class represents the structure of the test_data_tbl table in the database.
    It defines various columns to store different attributes of test data.

    Attributes:
        id (int): The unique identifier for each test data entry.
        conf_id (int): The ID of the associated API configuration.
        tc_id (str): The test case ID.
        params (str): The parameters for the API request.
        description (str): The description of the test data.
        method (str): The HTTP method used in the API request.
        request_body (dict): The request body of the API request.
        expected_response (str): The expected response for the API request.
        response_code (int): The expected HTTP response code.
        ignore_keys (str): Keys to ignore in the response comparison.
        test_suite (str): The test suite to which the test data belongs.
        error_schema (str): The schema for error responses.
        db_verification_query (str): The query to verify data in the database.
        is_datacleanup_required (bool): Indicates whether data cleanup is required after the test.
        datacleanup_query (str): The query to clean up data after the test.
        replacements (dict): Replacements for dynamic test data.
    """

    __tablename__ = "test_data_tbl"

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    conf_id = Column("CONF_ID", Integer)
    tc_id = Column("TC_ID", VARCHAR)
    params = Column("PARAMS", VARCHAR)
    description = Column("DESCRIPTION", VARCHAR, nullable=True)
    method = Column("METHOD", VARCHAR)
    request_body = Column("REQUEST_BODY", JSON)
    expected_response = Column("EXPECTED_RESPONSE", Text)
    response_code = Column("RESPONSE_CODE", Integer)
    ignore_keys = Column("IGNORE_KEYS", VARCHAR)
    test_suite = Column("TEST_SUITE", VARCHAR)
    error_schema = Column("ERROR_SCHEMA", Text)
    db_verification_query = Column("DB_VERIFICATION_QUERY", VARCHAR)
    is_datacleanup_required = Column("IS_DATACLEANUP_REQUIRED", Integer)
    datacleanup_query = Column("DATACLEANUP_QUERY", VARCHAR)
    replacements = Column("REPLACEMENTS", JSON)


engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
