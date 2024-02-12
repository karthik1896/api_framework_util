"""
Module for handling API configuration creation views.
"""
from __future__ import annotations
from fastapi import APIRouter
from pydantic import BaseModel
from utils import helper

# Create router instance
router = APIRouter(tags=["Create API Configuration"])


class CreateApiConfig(BaseModel):
    """
    Represents a configuration for creating an API.

    Attributes:
        app (str): The application associated with the API.
        module (str): The module associated with the API.
        sub_module (str): The sub_module associated with the API.
        api (str): The API endpoint.
        port (int, optional): The port number.
        internal_path (str): The internal path of the API.
        gateway_path (str): The gateway path of the API.
        db_details (str, optional): The database details.
        success_schema (str, optional): The success schema.
        internal_only (int): Flag indicating if the API is internal only.
    """

    app: str = "CFSSv2"
    module: str
    sub_module: str
    api: str
    port: int | None
    internal_path: str
    gateway_path: str
    db_details: str | None
    success_schema: str | None
    internal_only: int


@router.post("/Create/ApiConfig")
async def create_api_config(api_config: CreateApiConfig):
    """
    EndPoint Purpose :
    ```
    Create an API configuration based on the provided parameters.
    ```
    Sample Request :

    ```json
    {
      "app": "CFSSv2",
      "module": "Organization",
      "sub_module": "OrganizationListing",
      "api": "GetOrganizationList",
      "port": 31463,
      "internal_path": "/api/v1/Organization/GetOrganizationList",
      "gateway_path": "/api/v1/Organization/GetList",
      "db_details": "{}",
      "success_schema": "{}",
      "internal_only": 0
    }
    ```

    Sample Response :

    ```json
    {
      "api": "string",
      "message": "API Configured Successfully",
      "status_code": 200,
      "status_message": "Success"
    }
    ```

    """
    try:
        result = helper.create_api_configuration(
            api_config.app,
            api_config.module,
            api_config.sub_module,
            api_config.api,
            api_config.port,
            api_config.internal_path,
            api_config.gateway_path,
            api_config.db_details,
            api_config.success_schema,
            api_config.internal_only,
        )
        if result:
            return {
                "api": result,
                "message": "API Configured Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in create_api_config async method : {e}")
