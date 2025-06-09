from sqlmodel import SQLModel, Field, Column, INTEGER, NVARCHAR, SMALLINT, Boolean
from decimal import Decimal


class Product(SQLModel, table=True):
    __tablename__ = "Products"

    product_id: int | None = Field(
        default=None, sa_column=Column("ProductID", INTEGER, primary_key=True)
    )
    product_name: str = Field(
        sa_column=Column("ProductName", NVARCHAR(40), nullable=False)
    )
    supplier_id: int | None = Field(
        default=None, sa_column=Column("SupplierID", INTEGER, nullable=True)
    )
    category_id: int | None = Field(
        default=None, sa_column=Column("CategoryID", INTEGER, nullable=True)
    )
    quantity_per_unit: str | None = Field(
        default=None, sa_column=Column("QuantityPerUnit", NVARCHAR(20), nullable=True)
    )
    unit_price: Decimal | None = Field(
        default=None, sa_column=Column("UnitPrice", nullable=True)
    )
    units_in_stock: int | None = Field(
        default=None, sa_column=Column("UnitsInStock", SMALLINT, nullable=True)
    )
    units_on_order: int | None = Field(
        default=None, sa_column=Column("UnitsOnOrder", SMALLINT, nullable=True)
    )
    reorder_level: int | None = Field(
        default=None, sa_column=Column("ReorderLevel", SMALLINT, nullable=True)
    )
    discontinued: bool | None = Field(
        default=None, sa_column=Column("Discontinued", Boolean, nullable=True)
    )
    