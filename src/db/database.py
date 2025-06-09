from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import AsyncAdaptedQueuePool
from src.config import settings
from src.model import *

sqlserver_url = settings.database_url

engine = create_async_engine(
    sqlserver_url,
    echo=settings.DB_ECHO_LOG,
    future=True,
    pool_size=5,  
    max_overflow=10,  
    pool_timeout=30, 
    pool_pre_ping=True, 
    poolclass=AsyncAdaptedQueuePool, 
)


async def init_db():
    """
    Initialize the database schema.

    Creates all tables defined in SQLModel metadata if they don't exist.
    This function should be called during application startup to ensure
    the database structure is properly configured.

    The function uses a transaction to ensure schema creation is atomic.
    """

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)