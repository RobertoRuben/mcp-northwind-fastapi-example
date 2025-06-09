from abc import ABC, abstractmethod
from src.dto import ProductResponseDTO

class IProductService(ABC):
    
    @abstractmethod
    async def get_all_products(self) -> list[ProductResponseDTO]:
        """
        Retrieve all products.

        :return: A list of ProductResponseDTO objects representing all products.
        """
        pass
