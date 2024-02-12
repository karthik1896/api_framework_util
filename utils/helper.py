"""
Module containing functions for database operations, API configurations, and test data management.
"""
import numpy as np
import pandas as pd
from sqlalchemy import text
from models.api_configuration import ApiConfiguration, Session
from models.environment import Environment
from models.testdata import TestData
from utils.database_helper import (
    db_connect,
    update_table_data,
    query_data_from_db,
)


def create_api_configuration(
    application,
    module,
    sub_module,
    api,
    port,
    internal_path,
    gateway_path,
    db_details,
    success_schema,
    internal_only,
):
    """
    Create an API configuration entry in the database.

    Args:
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

    Returns:
        obj: The API configuration details.

    Raises:
        Exception: If an error occurs during data insertion.
    """
    try:
        session = Session()
        create_api_config = ApiConfiguration(
            application=application,
            module=module,
            sub_module=sub_module,
            api=api,
            port=port,
            internal_path=internal_path,
            gateway_path=gateway_path,
            db_details=db_details,
            success_schema=success_schema,
            internal_only=internal_only,
        )
        session.add(create_api_config)
        session.commit()
        return fetch_api_config_dtls(api)
    except Exception as e:
        print(f"Error inserting data into the api_configuration_mstr: {e}")
        return None


def fetch_env_dtls(env):
    """
    Fetch environment details based on the provided environment name.

    Args:
        env (str): The name of the environment to fetch details for.

    Returns:
        list: A list of environment details matching the provided environment name.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        session = Session()
        result = session.query(Environment).filter_by(env=env).all()
        return result
    except Exception as e:
        print(
            f"Error Fetching environment details, Error Occurred in fetch_env_dtls method: {e}"
        )
        return None


def fetch_all_env_dtls():
    """
    Fetch details of all environments from the database.

    Returns:
        list: A list of environment details.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        session = Session()
        result = session.query(Environment).all()
        return result
    except Exception as e:
        print(
            f"Error Fetching environment details, Error Occurred in fetch_all_env_dtls method : {e}"
        )
        return None


def fetch_applications():
    """
    Fetches a list of distinct application names from the database.

    Returns:
        dict: A dictionary containing the key 'APPLICATION' mapped to a list of application names.
            The list includes all distinct application names retrieved from the database, along with the value 'all'.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        query = "SELECT DISTINCT APPLICATION FROM env_tbl;"
        result = query_data_from_db(query)
        # Extract APPLICATION Values and place it in a list
        applications = [item["APPLICATION"] for item in result]
        # Append "all" value to the list
        applications.append("all")
        # Create a dictionary with the 'APPLICATION' key pointing to the list of applications
        result_dict = {"APPLICATION": applications}

        return result_dict
    except Exception as e:
        print(
            f"Error Fetching Applications, Error Occurred in fetch_applications method: {e}"
        )
        return None


def fetch_modules():
    """
    Fetches a list of distinct module names from the 'api_configuration_mstr' table.

    Returns:
        dict: A dictionary containing the key 'MODULE' mapped to a list of module names.
            The list includes all distinct module names retrieved from the database, along with the value 'all'.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        query = "SELECT DISTINCT MODULE FROM api_configuration_mstr;"
        result = query_data_from_db(query)
        # Extract MODULE Values and place it in a list
        modules = [item["MODULE"] for item in result]
        # Append "all" value to the list
        modules.append("all")
        # Create a dictionary with the 'MODULE' key pointing to the list of modules
        result_dict = {"MODULE": modules}

        return result_dict
    except Exception as e:
        print(f"Error Fetching Modules, Error Occurred in fetch_modules method: {e}")
        return None


def fetch_sub_modules(module):
    """
    Fetches a list of distinct sub_module names based on the provided module name.

    Args:
        module (str): The name of the module for which sub_module are to be fetched.

    Returns:
        dict: A dictionary containing the key 'SUB_MODULE' mapped to a list of sub-sub_module names.
            The list includes all distinct sub_module names retrieved from the database for the specified module,
            along with the value 'all'.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        query = f"SELECT DISTINCT A.SUB_MODULE FROM api_configuration_mstr A WHERE A.MODULE = CASE WHEN '{module}' = 'all' THEN A.MODULE ELSE '{module}' END;"
        result = query_data_from_db(query)
        # Extract SUB_MODULE Values and place it in a list
        sub_modules = [item["SUB_MODULE"] for item in result]
        # Append "all" value to the list
        sub_modules.append("all")
        # Create a dictionary with the 'SUB_MODULE' key pointing to the list of sub_modules
        result_dict = {"SUB_MODULE": sub_modules}
        return result_dict
    except Exception as e:
        print(
            f"Error Fetching SubModules, Error Occurred in fetch_sub_modules method: {e}"
        )
        return None


def fetch_api(sub_module):
    """
    Fetches a list of distinct API names based on the provided sub_module name.

    Args:
        sub_module (str): The name of the sub_module for which APIs are to be fetched.

    Returns:
        list: A list of distinct API names retrieved from the 'api_configuration_mstr' table
              for the specified sub_module.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        query = f"SELECT DISTINCT A.API FROM api_configuration_mstr A WHERE A.SUB_MODULE = CASE WHEN '{sub_module}' = 'all' THEN A.SUB_MODULE ELSE '{sub_module}' END;"
        result = query_data_from_db(query)
        # Extract SUB_MODULE Values and place it in a list
        api = [item["API"] for item in result]
        # Append "all" value to the list
        api.append("all")
        # Create a dictionary with the 'SUB_MODULE' key pointing to the list of sub_modules
        result_dict = {"API": api}
        return result_dict
    except Exception as e:
        print(f"Error Fetching APIs, Error Occurred in fetch_api method: {e}")
        return None


def fetch_all_api_config_dtls():
    """
    Fetches all API configuration details from the database.

    Returns:
        list: A list of all API configuration details retrieved from the database.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        session = Session()
        result = session.query(ApiConfiguration).all()
        return result
    except Exception as e:
        print(
            f"Error Fetching API Config Details, Error Occurred in fetch_all_api_config_dtls method : {e}"
        )
        return None


def fetch_api_config_dtls(api_name):
    """
    Fetches API configuration details for the specified API name from the database.

    Args:
        api_name (str): The name of the API for which configuration details are to be fetched.

    Returns:
        str: The configuration details of the specified API.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        session = Session()
        result = session.query(ApiConfiguration).filter_by(api=api_name).first()
        return result.api
    except Exception as e:
        print(
            f"Error Fetching API Config Details, Error Occurred in fetch_api_config_dtls method : {e}"
        )
        return None


def get_test_data_dropdown_list(app, module, sub_module):
    """
    Fetches dropdown list data for test data selection based on specified criteria.

    Args:
        app (str): The application name.
        module (str): The module name.
        sub_module (str): The sub_module name.

    Returns:
        dict: A dictionary containing dropdown list data for test data selection.
              The keys are 'APPLICATION', 'MODULE', 'SUB_MODULE', and 'API',
              and the corresponding values are lists of unique values for each category retrieved from the database.
              Each list includes all distinct values retrieved from the database for the specified criteria,
              along with the value 'all'.

    Raises:
        Exception: If an error occurs during the database query.
    """
    try:
        query = f"""
            SELECT A.APPLICATION, A.MODULE, A.SUB_MODULE, A.API
            FROM api_configuration_mstr A
            WHERE
                (A.APPLICATION = CASE WHEN '{app}' = 'all' THEN A.APPLICATION ELSE '{app}' END)
                AND
                (A.MODULE = CASE WHEN '{module}' = 'all' THEN A.MODULE ELSE '{module}' END)
                AND
                (A.SUB_MODULE = CASE WHEN '{sub_module}' = 'all' THEN A.SUB_MODULE ELSE '{sub_module}' END)
            GROUP BY A.APPLICATION, A.MODULE, A.SUB_MODULE, A.API;
        """
        result = query_data_from_db(query)

        if result:
            df = pd.DataFrame(result)
            response_dict = {key: [] for key in list(result[0].keys())}
            for col in df.columns:
                data = list(set(df[col]))
                data.append("all")
                response_dict[col] = data
            return response_dict
        # Handle the case where the query result is empty
        print("Query result is empty.")
        return []
    except Exception as e:
        print(
            f"Error Fetching TestData Dropdown values, Error Occurred in get_test_data_dropdown_list method : {e}"
        )
        return None


def create_test_data(
    conf_id,
    params,
    description,
    method,
    request_body,
    expected_response,
    response_code,
    ignore_keys,
    test_suite,
    error_schema,
    db_verification_query,
    is_datacleanup_required,
    datacleanup_query,
    replacements,
):
    """
    Creates a new test data entry in the database.

    Args:
        conf_id (int): The ID of the API configuration associated with the test data.
        params (str): The parameters for the API request.
        description (str): The description of the test data.
        method (str): The HTTP method for the API request (e.g., 'GET', 'POST').
        request_body (dict): The request body for the API request.
        expected_response (str): The expected response for the API request.
        response_code (int): The expected HTTP response code for the API request.
        ignore_keys (str): Keys to ignore in the response comparison.
        test_suite (str): The test suite to which the test data belongs.
        error_schema (str): The schema for error responses.
        db_verification_query (str): The query to verify data in the database.
        is_datacleanup_required (int): Indicates whether data cleanup is required after the test.
        datacleanup_query (str): The query to clean up data after the test.
        replacements (dict): Replacements for dynamic test data.

    Returns:
        bool or str: True if the test data is successfully inserted into the database,
                     otherwise, an error message is returned.

    Raises:
        Exception: If an error occurs during database operations.
    """
    session = Session()
    try:
        test_data = TestData(
            conf_id=conf_id,
            params=params,
            description=description,
            method=method,
            request_body=request_body,
            expected_response=expected_response,
            response_code=response_code,
            ignore_keys=ignore_keys,
            test_suite=test_suite,
            error_schema=error_schema,
            db_verification_query=db_verification_query,
            is_datacleanup_required=is_datacleanup_required,
            datacleanup_query=datacleanup_query,
            replacements=replacements,
        )
        session.add(test_data)
        session.commit()
        # Updating TC_ID after committing
        session.query(TestData).update(
            {TestData.tc_id: text("CONCAT('TC-', id)")}, synchronize_session=False
        )
        session.commit()
        return True
    except Exception as e:
        print(f"Error inserting data into the test_data_tbl: {e}")
        return f"Error inserting data into the test_data_tbl: {e}"


def upload_and_insert_excel(df):
    """
    Uploads and inserts data from a DataFrame into the test_data_tbl table in the database.

    Args:
        df (DataFrame): The DataFrame containing the data to be inserted into the database.

    Returns:
        str: A message indicating the success or failure of the data insertion/update.

    Raises:
        Exception: If an error occurs during data insertion/update or database operations.
    """
    # Replace NaN values with appropriate default values or handle them based on your use case
    df = df.replace({np.nan: None})

    # Drop the 'ID' column
    df = df.drop(["ID"], axis=1)

    # Create a connection to the MySQL database
    conn = db_connect()

    try:
        # Create a cursor object
        with conn.cursor() as cursor:
            for _, row in df.iterrows():
                # Strip leading and trailing spaces from each value in the row
                row = row.apply(lambda x: x.strip() if isinstance(x, str) else x)

                # Check for existing data based on CONF_ID and DESCRIPTION
                existing_query = "SELECT COUNT(*) FROM test_data_tbl WHERE CONF_ID = %s AND DESCRIPTION = %s"
                cursor.execute(existing_query, (row["CONF_ID"], row["DESCRIPTION"]))
                existing_data_count = cursor.fetchone()[0]

                if existing_data_count == 0:
                    # Insert new data if no existing data
                    placeholders = ", ".join(["%s"] * len(row))
                    columns = ", ".join(df.columns)
                    insert_query = (
                        f"INSERT INTO test_data_tbl({columns}) VALUES ({placeholders})"
                    )
                    cursor.execute(insert_query, tuple(row))
                    print(
                        f"Data inserted for CONF_ID: {row['CONF_ID']} and DESCRIPTION: {row['DESCRIPTION']}"
                    )
                else:
                    # Retrieve existing data from the database
                    select_existing_query = "SELECT * FROM test_data_tbl WHERE CONF_ID = %s AND DESCRIPTION = %s"
                    cursor.execute(
                        select_existing_query, (row["CONF_ID"], row["DESCRIPTION"])
                    )
                    existing_data = cursor.fetchone()

                    # Compare values and update if necessary
                    if existing_data:
                        update_columns = [
                            col
                            for col in df.columns
                            if col not in ["CONF_ID", "DESCRIPTION"]
                        ]
                        update_needed = any(
                            row[col] != existing_data[df.columns.get_loc(col)]
                            for col in update_columns
                        )

                        if update_needed:
                            # Construct the update query excluding CONF_ID and DESCRIPTION columns
                            update_query = f"UPDATE test_data_tbl SET {', '.join([f'{col} = %s' for col in update_columns])} WHERE CONF_ID = %s AND DESCRIPTION = %s"
                            cursor.execute(
                                update_query,
                                tuple(row[col] for col in update_columns)
                                + (row["CONF_ID"], row["DESCRIPTION"]),
                            )
                            print(
                                f"Data updated for CONF_ID: {row['CONF_ID']} and DESCRIPTION: {row['DESCRIPTION']}"
                            )
                        else:
                            print(
                                f"No changes for CONF_ID: {row['CONF_ID']} and DESCRIPTION: {row['DESCRIPTION']}"
                            )
        # Commit changes
        conn.commit()
        update_query = 'UPDATE test_data_tbl SET TC_ID=CONCAT("TC-",ID);'
        update_table_data(update_query)
        print("TestData successfully inserted/updated in the database.")
        return "TestData successfully inserted/updated in the database."

    except Exception as e:
        print("Error occurred during data insertion/update:", e)
        return f"Error occurred during data insertion/update: {e}"

    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")
