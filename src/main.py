from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from contextlib import asynccontextmanager
from src.db import init_db
from src.controller import product_router, product_tags_metadata

API_PREFIX = "/api/v1"

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan event handler for FastAPI.

    This function initializes the database when the application starts
    and cleans up resources when the application stops.

    Yields:
        None: The context manager does not yield any value.
    """
    await init_db()
    yield

app = FastAPI(
    title="Northwind API",
    version="1.0.0",
    description="API for Northwind database operations",
    openapi_tags=[product_tags_metadata],
    docs_url=API_PREFIX + "/docs",
    redoc_url=API_PREFIX + "/redoc",
)

mcp = FastApiMCP(
    app,
)

mcp.mount()

app.include_router(
    product_router,
    prefix=API_PREFIX,
)

mcp.setup_server()


