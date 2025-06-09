from urllib import response
from fastapi import APIRouter, Depends
from src.dto import ProductResponseDTO
from src.service.interfaces import IProductService
from src.service.dependencies import get_product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

product_tags_metadata = {
    "name": "Products",
    "description": "Operations with products",
}

@router.get(
    "",
    response_model=list[ProductResponseDTO],
    operation_id="get_all_products",
    summary="Get all products",
    status_code=201,
    responses={
        201: {
            "model": list[ProductResponseDTO],
            "description": "List of all products retrieved successfully.",
        },
    },
    description="Retrieves a list of all products from the database.",
)
async def get_all_products(
    product_service: IProductService = Depends(get_product_service)
) -> list[ProductResponseDTO]:
    """
    Get all products from the database.

    :param product_service: An instance of IProductService.
    :return: A list of ProductResponseDTO containing product details.
    """
    return await product_service.get_all_products()