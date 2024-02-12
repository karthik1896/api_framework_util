"""
Module for fetching All Environment details.
"""
from fastapi import APIRouter
from utils import helper

# Create router instance
router = APIRouter(tags=["Get All Environment Details"])


@router.get("/GetAll/Env")
async def get_all_env_details():
    """
    EndPoint Purpose :

    ```
    Retrieve all environment details.
    ```

    Sample Response :

    ```json
    {
      "data": [
        {
          "internal_url": "https://10.60.18.70",
          "application": "CFSSv2",
          "env": "QA",
          "password": "MTIzNDU=",
          "client_code": "CFSS",
          "signing_key": null,
          "encryption_algorithm": null,
          "client_type": "internal",
          "gateway": "https://cfssqaapi.muthootfinance.com",
          "id": 1,
          "username": "QA1",
          "login_url": "https://cfssqaapi.muthootfinance.com/api/v1/Session/Login",
          "client_secret": null,
          "encryption_type": null,
          "login_cred": "{\"userName\":\"QA3\",\"Password\":\"MTIzNDU=\"}",
          "login_type": "2"
        }
      ],
      "message": "Fetched all Environment Details Successfully",
      "status_code": 200,
      "status_message": "Success"
    }
    ```
    """
    try:
        env_dtls = helper.fetch_all_env_dtls()

        if env_dtls:
            return {
                "data": env_dtls,
                "message": "Fetched all Environment Details Successfully",
                "status_code": 200,
                "status_message": "Success",
            }
        return []
    except Exception as e:
        print(f"Error Occurred in get_all_env_details async method : {e}")
