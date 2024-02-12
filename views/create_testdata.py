"""
Module for handling TestData creation views.
"""
from __future__ import annotations
from io import BytesIO
import pandas as pd
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from utils import helper
from utils.helper import upload_and_insert_excel

# Create router instance
router = APIRouter(tags=["Create TestData"])


class CreateTestData(BaseModel):
    """
    Represents a configuration for creating test data.

    Attributes:
        conf_id (int): The configuration ID.
        params (str, optional): Additional parameters.
        description (str): The description of the test data.
        method (str): The HTTP method to be used.
        request_body (dict, optional): The request body.
        expected_response (str, optional): The expected response.
        response_code (int): The expected response code.
        ignore_keys (str): Keys to be ignored.
        test_suite (str): The test suite.
        error_schema (str, optional): The error schema.
        db_verification_query (str, optional): The database verification query.
        is_datacleanup_required (int): Flag indicating if data cleanup is required.
        datacleanup_query (str, optional): The data cleanup query.
        replacements (dict, optional): Replacements to be made.
    """

    conf_id: int
    params: str | None
    description: str
    method: str
    request_body: dict | None = {}
    expected_response: str | None
    response_code: int
    ignore_keys: str
    test_suite: str
    error_schema: str | None
    db_verification_query: str | None
    is_datacleanup_required: int
    datacleanup_query: str | None
    replacements: dict | None = {}


@router.post("/Create/TestData")
async def create_test_data(create: CreateTestData):
    """
    EndPoint Purpose :

    ```
    Create test data based on the provided configuration.
    ```
    Sample Request :

    ```json
    {
      "conf_id": 69,
      "params": "",
      "description": "Check whether API response is coming successfully when OrgLevelID given as 1 or 6",
      "method": "POST",
      "request_body": {"city": "", "email": "vinaya@emsyne.com", "gradeId": 3, "address1": "Ernakulam", "address2": "", "landmark": "", "postalId": 6856, "biometric": 0, "managerId": 1, "shortName": "TSQ", "inchargeId": 2, "languageId": 1, "orgLevelId": 5, "weeklyOff1": 1, "weeklyOff2": 2, "orgUnitCode": "TSQC6", "orgUnitName": "TESTINGQC6", "roManagerId": 3, "isCrmEnabled": 0, "isTppEnabled": 1, "parentUnitID": 38, "repaymentMsg": 1, "isHillStation": 1, "unitAreaTypeId": 1, "workingShiftId": 1, "auctionCenterId": 1933, "isAdvanceOtpRqd": 1, "isClosureOtpRqd": 0, "sortingCenterId": 1, "unitOpeningDate": "2023-12-28", "htmlPhotoCapture": 0, "roAuditManagerId": 2, "unitMobileNumber": "+919874561232", "populationGroupId": 2, "localPoliceStation": "Ekm", "unitLandlineNumber": "23456789", "managerMobileNumber": "", "cashierPrintTerminal": 0, "isGoldVerificationRqd": 1, "managerLandlineNumber": "", "isOrnamentImageMandatory": 1, "loginValidationDisabledTill": "2023-12-30", "localAdministrationAuthorityId": 2},
      "expected_response": {"data":{"id":10914},"statusCode":"200","statusMessage":"Success","correlationId":"01HMQS3H6QM07MYN6FARZ35MF5"},
      "response_code": 200,
      "ignore_keys": "['correlationId','data']",
      "test_suite": "Functional",
      "error_schema": {},
      "db_verification_query": "",
      "is_datacleanup_required": 1,
      "datacleanup_query": {"type":"sp","query":"CFSSV2_QA_AUTOMATION.SP_ORGUNIT_DATA_CLEANUP","input":["TSQC6"]},
      "replacements": {}
    }
    ```

    Sample Response :

    ```json
    {
      "data": true,
      "message": "TestData Imported Successfully",
      "status_code": 200,
      "status_message": "Success"
    }
    ```

    """
    try:
        create = helper.create_test_data(
            create.conf_id,
            create.params,
            create.description,
            create.method,
            create.request_body,
            create.expected_response,
            create.response_code,
            create.ignore_keys,
            create.test_suite,
            create.error_schema,
            create.db_verification_query,
            create.is_datacleanup_required,
            create.datacleanup_query,
            create.replacements,
        )
        if create:
            return {
                "data": create,
                "message": "TestData Imported Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in create_test_data async method : {e}")


@router.post("/BulkInsert/TestData")
async def create_upload_file(file: UploadFile = File(...)):
    """
    EndPoint Purpose :

    ```
    Upload and insert test data from the provided file.
    ```
    Sample Request :

    ```
    multipart/form-data
    ```

    Sample Response :

    ```json
    {
      "data": [
                {
                  "filename": "testdata.csv",
                  "message": "TestData successfully inserted/updated in the database."
                }
              ],
      "status_code": 200
    }
    ```

    """
    try:
        # Read the file into memory
        content = await file.read()

        # Convert the file content to a Pandas DataFrame
        if file.filename.endswith(".csv"):
            df = pd.read_csv(BytesIO(content))
        elif file.filename.endswith((".xls", ".xlsx")):
            df = pd.read_excel(BytesIO(content))
        else:
            return {"error": "Unsupported file format"}
        resp_mess = upload_and_insert_excel(df)
        return {
            "data": [{"filename": file.filename, "message": resp_mess}],
            "status_code": 200,
        }
    except Exception as e:
        print(f"Error Occurred in create_upload_file async method : {e}")
