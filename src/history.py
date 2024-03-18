from typing import Optional

from src.order import Order
from src.product import Product


class SalesHistory:
    def __init__(self, orders: list[Order] = None):
        self.orders = orders if orders else []

    def add_order(self, order: Order):
        self.orders.append(order)

    def get_orders_by_product(self, product: Product) -> Optional[list[Order]]:
        return [order for order in self.orders if order.has_product(product)]
