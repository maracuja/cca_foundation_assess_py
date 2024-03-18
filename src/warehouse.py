from dataclasses import dataclass
from src.product import Product


class InsufficientStockError(Exception):
    pass


@dataclass
class Entry:
    product: Product
    stock: int


@dataclass
class Warehouse:
    catalogue: list[Entry]

    def check_stock(self, product: Product) -> int:
        for entry in self.catalogue:
            if entry.product == product:
                return entry.stock

    def adjust_stock(self, product: Product, quantity: int):
        for entry in self.catalogue:
            if entry.product == product:
                if quantity > entry.stock:
                    raise InsufficientStockError(
                        f"Trying to deduct {quantity}, but only {entry.stock} in stock."
                    )
                entry.stock -= quantity
