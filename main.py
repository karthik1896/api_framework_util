"""
Main module to run the FastAPI application.
"""
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from configurations.config import api_port
from views import (
    create_api_config,
    create_testdata,
    get_all_api_config_details,
    get_all_env_details,
    get_env_details,
    get_testdata,
    dropdown,
)

app = FastAPI(
    title="API Framework Utility",
    description="Utility for Test API Framework",
    version="1.0.0",
)
origins = ["*"]
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(create_api_config.router)
app.include_router(create_testdata.router)
app.include_router(dropdown.router)
app.include_router(get_all_api_config_details.router)
app.include_router(get_all_env_details.router)
app.include_router(get_env_details.router)
app.include_router(get_testdata.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=api_port, reload=True)
