"""
Module for fetching TestData details.
"""
from fastapi import APIRouter
from pydantic import BaseModel
from utils import database_helper

# Create router instance
router = APIRouter(tags=["Get TestData"])


class FetchTestData(BaseModel):
    """
    Represents a configuration for fetching test data.

    Attributes:
        app (str): The application associated with the test data.
        module (str): The module associated with the test data.
        sub_module (str): The sub_module associated with the test data.
        api (str): The API associated with the test data.
        test_suite (str): The test suite associated with the test data.
        env (str): The environment associated with the test data.
        client_type (str): The client type associated with the test data.
        service_type (str): The service type associated with the test data.
    """

    app: str = "CFSSv2"
    module: str = "all"
    sub_module: str = "all"
    api: str = "all"
    test_suite: str = "all"
    env: str = "QA"
    client_type: str = "internal"
    service_type: str = "gateway"


@router.post("/Get/TestData")
async def get_testdata(test_data: FetchTestData):
    """
    EndPoint Purpose :

    ```
    Retrieve test data based on the provided configuration.
    ```

    Sample Request :

    ```json
    {
      "app": "CFSSv2",
      "module": "Organization",
      "sub_module": "OrganizationCreation",
      "api": "GetSortingCenter",
      "test_suite": "all",
      "env": "QA",
      "client_type": "internal",
      "service_type": "gateway"
    }
    ```

    Sample Response :

    ```json
    {
      "data": [
        {
          "APPLICATION": "CFSSv2",
          "MODULE": "Organization",
          "SUB_MODULE": "OrganizationCreation",
          "API": "GetSortingCenter",
          "DB_DETAILS": null,
          "DESCRIPTION": "Check whether API Response is coming successfully when valid auctionCenterId is given",
          "METHOD": "POST",
          "REQUEST_BODY": "{\"auctionCenterId\": 1812}",
          "EXPECTED_RESPONSE": "{\"data\":[{\"sortingCenterId\":1,\"sortingCenterName\":\"ERNAKULAM\"},{\"sortingCenterId\":2,\"sortingCenterName\":\"IDUKKI\"},{\"sortingCenterId\":3,\"sortingCenterName\":\"TRISUR\"},{\"sortingCenterId\":4,\"sortingCenterName\":\"KOLLAM, KOLLAMDIST, KERALA - 696969\"}],\"statusCode\":\"200\",\"statusMessage\":\"Success\",\"correlationId\":\"01HMQNW9KC01PZCBFVRHHD9CSQ\"}",
          "RESPONSE_CODE": 200,
          "DB_VERIFICATION_QUERY": null,
          "IGNORE_KEYS": "['correlationId']",
          "TC_ID": "TC-729",
          "ID": 729,
          "TEST_SUITE": "Functional",
          "REPLACEMENTS": null,
          "SUCCESS_SCHEMA": "{\"type\":\"object\",\"properties\":{\"data\":{\"type\":\"array\",\"items\":{\"type\":\"object\",\"properties\":{\"sortingCenterId\":{\"type\":\"integer\"},\"sortingCenterName\":{\"type\":\"string\"}},\"required\":[\"sortingCenterId\",\"sortingCenterName\"]}},\"statusCode\":{\"type\":\"string\"},\"statusMessage\":{\"type\":\"string\"},\"correlationId\":{\"type\":\"string\"}},\"required\":[\"data\",\"statusCode\",\"statusMessage\",\"correlationId\"]}",
          "ERROR_SCHEMA": null,
          "IS_DATACLEANUP_REQUIRED": null,
          "DATACLEANUP_QUERY": null,
          "USERNAME": "QA1",
          "PASSWORD": "MTIzNDU=",
          "LOGIN_URL": "https://cfssqaapi.muthootfinance.com/api/v1/Session/Login",
          "client_code": "CFSS",
          "client_secret": null,
          "signing_key": null,
          "encryption_type": null,
          "encryption_algorithm": null,
          "login_cred": "{\"userName\":\"QA3\",\"Password\":\"MTIzNDU=\"}",
          "client_type": "internal",
          "login_type": "2",
          "URL": "https://cfssqaapi.muthootfinance.com/api/v1/Organization/GetSortingCenter"
        },
      ],
      "message": "Fetched TestData Successfully",
      "status_code": 200,
      "status_message": "Success"
    }


    """
    try:
        test_data = database_helper.query_data_from_sp(
            "CALL GET_API_TEST_DATA(%s, %s, %s, %s, %s, %s, %s, %s)",
            test_data.app,
            test_data.module,
            test_data.sub_module,
            test_data.api,
            test_data.test_suite,
            test_data.env,
            test_data.client_type,
            test_data.service_type,
        )
        if test_data:
            return {
                "data": test_data,
                "message": "Fetched TestData Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_testdata async method : {e}")
