from src.dto import ProductResponseDTO
from src.service.interfaces import IProductService
from src.repository.interfaces import IProductRepository

class ProductServiceImpl(IProductService):
    def __init__(self, product_repository: IProductRepository):
        """
        Initialize the ProductServiceImpl with a product repository.

        :param product_repository: An instance of IProductRepository.
        """
        self.product_repository = product_repository

    async def get_all_products(self) -> list[ProductResponseDTO]:
        products = await self.product_repository.get_all()
        return [
            ProductResponseDTO(
                product_id=product.product_id,
                product_name=product.product_name,
                supplier_id=product.supplier_id,
                category_id=product.category_id,
                quantity_per_unit=product.quantity_per_unit,
                unit_price=product.unit_price,
                units_in_stock=product.units_in_stock,
                units_on_order=product.units_on_order,
                reorder_level=product.reorder_level,
                discontinued=product.discontinued,  
            )
            for product in products
        ]