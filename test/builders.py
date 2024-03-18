from typing import Self

from src.address import Address
from src.countries import Country
from src.order import Item, Order
from src.product import Product


class OrderBuilder:
    def __init__(self, order_id: str, country: Country = None):
        self.order_id = order_id
        self.country: Country = country if country else Country.UNITED_KINGDOM
        self.products: list[Product] = []

    def with_address(self, country: Country) -> Self:
        self.country = country
        return self

    def with_products(self, products: list[Product]) -> Self:
        self.products = products
        return self

    def build(self) -> Order:
        address = Address(
            address_id="ADDRESS_1",
            house="45",
            street="My Street",
            city="London",
            postcode="AB3 4EF",
            country=self.country,
        )

        return Order(
            order_id=self.order_id,
            shipping_address=address,
            items=[Item(product=product, quantity=1) for product in self.products],
        )
