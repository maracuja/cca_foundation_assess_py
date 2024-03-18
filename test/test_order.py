import unittest

from src.order import Item, Order
from src.product import Product
from src.address import Address
from src.countries import Country


class OrderTest(unittest.TestCase):
    def test_initialise_order(self):
        address = Address(
            house="45",
            street="My Street",
            city="London",
            postcode="AB3 4EF",
            country=Country.UNITED_KINGDOM,
        )
        order = Order(shipping_address=address, items=[])
        assert len(order.items) == 0

    def test_add_item_to_order(self):
        product = Product(id=1, description="Celtic Jersey", price=49.99)
        item = Item(product=product, quantity=1)
        address = Address(
            house="45",
            street="My Street",
            city="London",
            postcode="AB3 4EF",
            country=Country.UNITED_KINGDOM,
        )
        order = Order(shipping_address=address, items=[])
        order.add_item(item)
        assert len(order.items) == 1
