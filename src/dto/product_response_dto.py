from pydantic import BaseModel, Field
from decimal import Decimal

class ProductResponseDTO(BaseModel):
    product_id: int = Field(..., description="Unique identifier for the product")
    product_name: str = Field(..., description="Name of the product")
    supplier_id: int | None = Field(
        None, description="Identifier for the supplier of the product"
    )
    category_id: int | None = Field(
        None, 
        description="Identifier for the category of the product",
        examples=[1]
    )
    quantity_per_unit: str | None = Field(
        None, 
        description="Quantity of the product per unit",
        examples=["10 boxes"]
    )
    unit_price: Decimal | None = Field(
        None, 
        description="Price of the product per unit",
        examples=[19.99]
    )
    units_in_stock: int | None = Field(
        None, 
        description="Number of units of the product in stock",
        examples=[100]
    )
    units_on_order: int | None = Field(
        None, 
        description="Number of units of the product on order",
        examples=[50]
    )
    reorder_level: int | None = Field(
        None, 
        description="Reorder level for the product",
        examples=[20]
    )
    discontinued: bool | None = Field(
        None, 
        description="Indicates if the product is discontinued",
        examples=[False]
    )
    
    