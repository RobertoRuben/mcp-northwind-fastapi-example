from math import prod
from unittest import result
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from src.model import Product
from src.repository.decorators import transactional
from src.repository.interfaces import IProductRepository
from src.exception.invalid_field_exception import InvalidFieldException


class ProductRepositoryImpl(IProductRepository):

    def __init__(self, session: AsyncSession):
        """
        Initialize the ProductRepositoryImpl with an AsyncSession.        :param session: An instance of AsyncSession for database operations.
        """
        self.session = session

    @transactional(readonly=True)
    async def get_all(self) -> list[Product]:
        stmt = select(Product)
        result = await self.session.exec(stmt)
        products = result.all()
        return list(products)
