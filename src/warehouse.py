from dataclasses import dataclass

from src.history import SalesHistory
from src.product import Product


class InsufficientStockError(Exception):
    pass


class ProductNotFoundError(Exception):
    pass


@dataclass
class Entry:
    product: Product
    stock: int


class Warehouse:
    def __init__(self, catalogue: dict[int, Entry], sales_history: SalesHistory = None):
        self.catalogue: dict[int, Entry] = catalogue
        self.sales_history: SalesHistory = (
            sales_history if sales_history else SalesHistory()
        )

    def add_entry(self, entry: Entry):
        if entry.product.id in self.catalogue:
            self.receive_stock(entry.product, entry.stock)
        else:
            self.catalogue[entry.product.id] = entry

    def get_entry(self, product: Product):
        entry = self.catalogue.get(product.id)
        if not entry:
            raise ProductNotFoundError(
                f"There is no {product.description} in the warehouse."
            )
        return entry

    def check_stock(self, product: Product) -> int:
        return self.get_entry(product).stock

    def adjust_stock(self, product: Product, quantity: int):
        entry = self.get_entry(product)
        if quantity > entry.stock:
            raise InsufficientStockError(
                f"Trying to deduct {quantity}, but only {entry.stock} in stock."
            )
        entry.stock -= quantity

    def receive_stock(self, product: Product, quantity: int):
        self.get_entry(product).stock += quantity

    def confirm_order(self, order):
        for item in order.items:
            self.adjust_stock(item.product, item.quantity)
        self.sales_history.add_order(order)
