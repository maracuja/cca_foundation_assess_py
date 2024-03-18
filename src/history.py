from dataclasses import dataclass
from src.order import Order


class SalesHistory:
    def __init__(self, orders: list[Order] = None):
        self.orders = orders if orders else []

    def add_order(self, order: Order):
        self.orders.append(order)
