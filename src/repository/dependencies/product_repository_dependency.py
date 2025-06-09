from fastapi import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.db.dependencies import get_async_session
from src.repository.interfaces import IProductRepository
from src.repository.implementations import ProductRepositoryImpl

async def get_product_repository(
    session: AsyncSession = Depends(get_async_session)
) -> IProductRepository:
    """
    Dependency to provide an instance of ProductRepositoryImpl.

    :param session: An instance of AsyncSession for database operations.
    :return: An instance of IProductRepository.
    """
    return ProductRepositoryImpl(session = session)