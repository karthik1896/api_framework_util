"""
Module for handling dropdown-related views.
"""
from __future__ import annotations
from fastapi import APIRouter
from pydantic import BaseModel
from utils import helper

# Create router instance
router = APIRouter(tags=["Dropdowns"])


class Dropdown(BaseModel):
    """
    Represents a dropdown menu configuration.

    Attributes:
        APPLICATION (str): The application associated with the dropdown.
        MODULE (str): The module associated with the dropdown.
        SUB_MODULE (str): The sub_module associated with the dropdown.
        API (str): The API associated with the dropdown.
    """

    APPLICATION: str | None = "CFSSv2"
    MODULE: str | None = "all"
    SUB_MODULE: str | None = "all"
    API: str | None = "all"


class Module(BaseModel):
    """
    Represents a module dropdown.

    Attributes:
        MODULE (str): The name of the module.
    """

    MODULE: str | None = "all"


class SubModule(BaseModel):
    """
    Represents a sub_module dropdown.

    Attributes:
        SUB_MODULE (str): The name of the module.
    """

    SUB_MODULE: str | None = "all"


@router.post("/Get/TestDataDDL")
async def get_test_data_dropdown(dropdown: Dropdown):
    """
      EndPoint Purpose :

      ```
      Retrieve test data dropdown values based on the provided dropdown configuration.
      ```
      Sample Request :

      ```json
      {
        "APPLICATION": "CFSSv2",
        "MODULE": "all",
        "SUB_MODULE": "all",
        "API": "all"
      }
      ```
      Sample Response :

      ```json
      {
    "data": {
      "APPLICATION": [
        "CFSSv2",
        "all"
      ],
      "MODULE": [
        "MasterService",
        "all"
      ],
      "SUB_MODULE": [
        "testsubmodule1",
        "UserCreation",
        "HolidayCreation",
        "all"
      ],
      "API": [
        "Yearlist",
        "GetSubCategories",
        "all"
      ]
    },
    "message": "Fetched TestData Dropdown values Successfully",
    "status_code": 200,
    "status_message": "Success"
      }

    """
    try:
        testdata_ddl = helper.get_test_data_dropdown_list(
            dropdown.APPLICATION, dropdown.MODULE, dropdown.SUB_MODULE
        )
        if testdata_ddl:
            return {
                "data": testdata_ddl,
                "message": "Fetched TestData Dropdown values Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_test_data_dropdown async method : {e}")


@router.get("/Get/Application")
async def get_application_dropdown():
    """
    EndPoint Purpose :

    ```
    Retrieve application dropdown values.
    ```
    Sample Response :

    ```json
    {
      "data": {
        "APPLICATION": [
          "CFSSv2",
          "all"
        ]
      },
      "message": "Fetched Application Dropdown values Successfully",
      "status_code": 200,
      "status_message": "Success"
    }
    ```

    """
    try:
        application = helper.fetch_applications()
        if application:
            return {
                "data": application,
                "message": "Fetched Application Dropdown values Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_application_dropdown async method : {e}")


@router.get("/Get/Modules")
async def get_module_dropdown():
    """
    EndPoint Purpose :

    ```
    Retrieve module dropdown values.
    ```
    Sample Response :

    ```json
    {
      "data": {
        "MODULE": [
          "Organization",
          "Product",
          "all"
        ]
      },
      "message": "Fetched Module Dropdown values Successfully",
      "status_code": 200,
      "status_message": "Success"
    }
    ```

    """
    try:
        modules = helper.fetch_modules()
        if modules:
            return {
                "data": modules,
                "message": "Fetched Module Dropdown values Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_module_dropdown async method : {e}")


@router.post("/Get/SubModules")
async def get_sub_module_dropdown(module: Module):
    """
      EndPoint Purpose :

      ```
      Retrieve sub_module dropdown values.
      ```

      Sample Request :

      ```json
      {
      "MODULE": "all"
      }
      ```
      Sample Response :

      ```json
      {
    "data": {
      "SUB_MODULE": [
        "OrganizationListing",
        "ProductCreation",
        "all"
      ]
    },
    "message": "Fetched Sub_Module Dropdown values Successfully",
    "status_code": 200,
    "status_message": "Success"
      }
      ```

    """
    try:
        sub_module = helper.fetch_sub_modules(module.MODULE)
        if sub_module:
            return {
                "data": sub_module,
                "message": "Fetched Sub_Module Dropdown values Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_sub_module_dropdown async method : {e}")


@router.post("/Get/APIs")
async def get_api_dropdown(sub_module: SubModule):
    """
      EndPoint Purpose :

      ```
      Retrieve api dropdown values.
      ```

      Sample Request :

      ```json
      {
      "SUB_MODULE": "all"
      }
      ```

      Sample Response :

      ```json
      {
    "data": {
      "API": [
        "GetOrganizationList",
        "GetCategories",
        "GetCollaterals",
        "all"
            ]
            },
    "message": "Fetched API Dropdown values Successfully",
    "status_code": 200,
    "status_message": "Success"
      }
      ```
    """
    try:
        api = helper.fetch_api(sub_module.SUB_MODULE)
        if api:
            return {
                "data": api,
                "message": "Fetched API Dropdown values Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_sub_module_dropdown async method : {e}")
