from dataclasses import dataclass
from src.product import Product


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
                entry.stock += quantity
