"""
Module for database operations and queries.
"""
import json
import mysql.connector
from configurations.config import (
    database_host,
    database_username,
    database_password,
    database_schema,
)


def db_connect():
    """
    Connect to the MySQL database.

    Returns:
        MySQLConnection: A connection object to the MySQL database, or None if connection fails.
    """
    try:
        print("Connecting to MySQL Database")
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host=database_host,
            user=database_username,
            password=database_password,
            database=database_schema,
        )
        print("Successfully Connected to MySQL Database")
        return conn
    except Exception as e:
        print("Exception Occurred in db_connect method :", e)
        return None  # Return None if connection fails


def query_data_from_sp(
    query,
    app,
    module,
    sub_module,
    api,
    test_suite,
    env,
    client_type,
    service_type,
) -> list[dict]:
    """
    Query data from the database based on the provided stored procedure query and parameters.

    Args:
        query (str): The stored procedure query to fetch the data.
        app (str): The application associated with the test data.
        module (str): The module associated with the test data.
        sub_module (str): The sub_module associated with the test data.
        api (str): The API associated with the test data.
        test_suite (str): The test suite associated with the test data.
        env (str): The environment associated with the test data.
        client_type (str): The client type associated with the test data.
        service_type (str): The service type associated with the test data.

    Returns:
        list[dict]: A list of dictionaries containing the fetched data.

    Raises:
        Exception: If there is an error executing the query or fetching the results.
    """
    try:
        # Create a connection to the MySQL database
        conn = db_connect()

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the SQL query
        print(f"Executing stored procedure query: {query}")
        cursor.execute(
            query,
            (app, module, sub_module, api, test_suite, env, client_type, service_type),
        )

        # Fetch all rows from the result set and return them as a list of tuples
        print("Fetching Test Data by query_data_from_sp method")
        results = cursor.fetchall()

        # Convert the list of tuples to dict
        column_names = [col[0] for col in cursor.description]
        data = [dict(zip(column_names, row)) for row in results]
        print("Fetched Test Data Successfully by query_data_from_sp method")
        return data

    except Exception as e:
        print(f"Error querying data from the database: {str(e)}")
        raise Exception(f"Error querying data from the database: {str(e)}") from e

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


def insert_data_into_db(query, values=None) -> None:
    """
    Execute an SQL insert query with optional values and commit the transaction.

    Args:
        query (str): The SQL query to insert data into the database.
        values (tuple, optional): Values to be inserted into the database. Defaults to None.

    Raises:
        Exception: If there is an error executing the query or committing the transaction.
    """
    try:
        conn = db_connect()
        print(f"Executing SQL query: {query}")
        cursor = conn.cursor()

        # Serialize dictionary values to JSON
        if values:
            values = tuple(
                json.dumps(value) if isinstance(value, dict) else value
                for value in values
            )

        # Execute the SQL query with values if provided
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        conn.commit()
        print("Inserted Data into Database Successfully")

    except Exception as e:
        print(f"Error inserting data into the database: {str(e)}")
        raise Exception(f"Error inserting data into the database: {str(e)}") from e

    finally:
        cursor.close()
        conn.close()


def update_table_data(query):
    """
    Execute an SQL update query and commit the transaction.

    Args:
        query (str): The SQL query to update data in the database.

    Raises:
        Exception: If there is an error executing the query or committing the transaction.
    """
    try:
        conn = db_connect()
        print(f"Executing SQL query: {query}")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print(cursor.rowcount, "record(s) affected")

    except Exception as e:
        print(f"Error inserting data into the database: {str(e)}")
        raise Exception(f"Error inserting data into the database: {str(e)}") from e


def query_data_from_db(query) -> list[dict]:
    """
    Query data from the database based on the provided SQL query.

    Args:
        query (str): The SQL query to fetch the data.

    Returns:
        list[dict]: A list of dictionaries containing the fetched data.

    Raises:
        Exception: If there is an error executing the query or fetching the results.
    """
    try:
        # Create a connection to the MySQL database
        conn = db_connect()

        print(f"Executing SQL query: {query}")

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all rows from the result set and return them as a list of tuples
        results = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]
        data = [dict(zip(column_names, row)) for row in results]

        return data

    except Exception as e:
        print(f"Error querying data from the database: {str(e)}")
        raise Exception(f"Error querying data from the database: {str(e)}") from e

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
