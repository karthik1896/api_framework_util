"""
Module for fetching API configuration details.
"""
from fastapi import APIRouter
from utils import helper

# Create router instance
router = APIRouter(tags=["Get API Config Details"])


@router.get("/GetAll/ApiConfig")
async def get_all_api_config_details():
    """
    EndPoint Purpose :

    ```
    Retrieve all API configuration details.
    ```

    Sample Response :

    ```json

    {
      "data": [
        {
          "sub_module": "OrganizationListing",
          "conf_id": 1,
          "application": "CFSSv2",
          "port": 31463,
          "gateway_path": "/api/v1/Organization/GetList",
          "success_schema": "{\"type\": \"object\", \"required\": [\"data\", \"statusCode\", \"statusMessage\", \"correlationId\"], \"properties\": {\"data\": {\"type\": \"object\", \"required\": [\"currentPage\", \"totalPages\", \"perPage\", \"recordsTotal\", \"list\"], \"properties\": {\"list\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"required\": [\"orgLevel\", \"orgunitId\", \"orgunitCode\", \"orgunitName\", \"parentUnitCode\", \"parentUnitName\", \"unitContact\", \"managerContact\", \"statusId\", \"statusName\", \"mergedDate\", \"mergedUnit\", \"closedDate\"], \"properties\": {\"orgLevel\": {\"type\": \"string\"}, \"statusId\": {\"type\": \"integer\"}, \"orgunitId\": {\"type\": \"integer\"}, \"closedDate\": {\"type\": \"null\"}, \"mergedDate\": {\"type\": \"null\"}, \"mergedUnit\": {\"type\": \"null\"}, \"statusName\": {\"type\": \"string\"}, \"orgunitCode\": {\"type\": \"string\"}, \"orgunitName\": {\"type\": \"string\"}, \"unitContact\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"required\": [\"contact\", \"type\"], \"properties\": {\"type\": {\"type\": \"string\"}, \"contact\": {\"type\": \"null\"}}}}, \"managerContact\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"required\": [\"contact\", \"type\"], \"properties\": {\"type\": {\"type\": \"string\"}, \"contact\": {\"type\": \"null\"}}}}, \"parentUnitCode\": {\"type\": \"string\"}, \"parentUnitName\": {\"type\": \"string\"}}}}, \"perPage\": {\"type\": \"integer\"}, \"totalPages\": {\"type\": \"integer\"}, \"currentPage\": {\"type\": \"integer\"}, \"recordsTotal\": {\"type\": \"integer\"}}}, \"statusCode\": {\"type\": \"string\"}, \"correlationId\": {\"type\": \"string\"}, \"statusMessage\": {\"type\": \"string\"}}}",
          "module": "Organization",
          "api": "GetOrganizationList",
          "internal_path": "/api/v1/Organization/GetOrganizationList",
          "db_details": null,
          "internal_only": 0
        },
        {
          "sub_module": "ProductCreation",
          "conf_id": 2,
          "application": "CFSSv2",
          "port": 31033,
          "gateway_path": null,
          "success_schema": "{\"type\": \"object\", \"required\": [\"data\", \"statusCode\", \"statusMessage\", \"correlationId\"], \"properties\": {\"data\": {\"type\": \"array\", \"items\": {\"type\": \"object\", \"required\": [\"id\", \"name\"], \"properties\": {\"id\": {\"type\": \"integer\"}, \"name\": {\"type\": \"string\"}}}}, \"statusCode\": {\"type\": \"string\"}, \"correlationId\": {\"type\": \"string\"}, \"statusMessage\": {\"type\": \"string\"}}}",
          "module": "Product",
          "api": "GetCategories",
          "internal_path": "/api/v1/Product/GetCategories",
          "db_details": null,
          "internal_only": 1
        }
      ],
      "message": "Fetched all API Config Successfully",
      "status_code": 200,
      "status_message": "Success"
    }
    ```
    """
    try:
        env_dtls = helper.fetch_all_api_config_dtls()

        if env_dtls:
            return {
                "data": env_dtls,
                "message": "Fetched all API Config Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_all_api_config_details async method : {e}")
