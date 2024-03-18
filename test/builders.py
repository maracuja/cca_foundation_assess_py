from typing import Self

from src.address import Address
from src.countries import Country
from src.order import Item, Order
from src.product import Product


class AddressBuilder:
    def __init__(self, address_id: str, country: Country = None):
        self.address_id: str = address_id
        self.country: Country = country if country else Country.UNITED_KINGDOM

    def build(self) -> Address:
        return Address(
            address_id=self.address_id,
            house="45",
            street="My Street",
            city="London",
            postcode="AB3 4EF",
            country=self.country,
        )


class OrderBuilder:
    def __init__(self, order_id: str, country: Country = None):
        self.order_id = order_id
        self.country: Country = country if country else Country.UNITED_KINGDOM
        self.products: list[Product] = []
        self.address_id: str = "ADDRESS_1"

    def with_country(self, country: Country) -> Self:
        self.country = country
        return self

    def with_address(self, address_id: str) -> Self:
        self.address_id = address_id
        return self

    def with_products(self, products: list[Product]) -> Self:
        self.products = products
        return self

    def build(self) -> Order:
        return Order(
            order_id=self.order_id,
            shipping_address=AddressBuilder(
                address_id=self.address_id,
                country=self.country,
            ).build(),
            items=[Item(product=product, quantity=1) for product in self.products],
        )
