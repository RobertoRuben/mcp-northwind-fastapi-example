from fastapi import Depends
from src.service.interfaces import IProductService
from src.service.implementations import ProductServiceImpl
from src.repository.interfaces import IProductRepository
from src.repository.dependencies import get_product_repository

async def get_product_service(
    repository: IProductRepository = Depends(get_product_repository)
) -> IProductService:
    """
    Dependency injection for ProductServiceImpl.

    :param product_repository: An instance of IProductRepository.
    :return: An instance of IProductService.
    """
    return ProductServiceImpl(product_repository=repository)