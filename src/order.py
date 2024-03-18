from dataclasses import dataclass

from src.address import Address
from src.product import Product
from src.shipping import calculate_shipping


@dataclass
class Item:
    product: Product
    quantity: int

    def get_subtotal(self):
        return self.product.price * self.quantity


@dataclass
class Order:
    order_id: str
    shipping_address: Address
    items: list[Item]

    def add_item(self, item: Item):
        self.items.append(item)

    def get_total(self):
        total = sum(item.get_subtotal() for item in self.items)
        shipping = calculate_shipping(self.shipping_address.country.value, total)
        return total + shipping
