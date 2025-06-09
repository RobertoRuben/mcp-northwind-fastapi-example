from abc import ABC, abstractmethod
from src.model import Product

class IProductRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Product]:
        """
        Retrieve all products from the repository.

        Returns:
            list[Product]: A list of Product instances.
        """
        pass