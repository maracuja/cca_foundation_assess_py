from dataclasses import dataclass
import pytest

from src.order import Item
from src.product import Product
from src.countries import Country

from test.builders import OrderBuilder


def test_initialise_order():
    order = OrderBuilder(order_id="ORDER_1").build()
    assert len(order.items) == 0


def test_add_item_to_order():
    product = Product(id=1, description="Celtic Jersey", price=49.99)
    item = Item(product=product, quantity=1)
    order = OrderBuilder(order_id="ORDER_1").build()
    order.add_item(item)
    assert len(order.items) == 1


def test_order_has_product():
    product_1 = Product(id=1, description="Celtic Jersey", price=49.99)
    product_2 = Product(id=2, description="Rangers Jersey", price=0.01)
    item = Item(product=product_1, quantity=1)
    order = OrderBuilder(order_id="ORDER_1").build()
    order.add_item(item)
    assert order.has_product(product_1) is True
    assert order.has_product(product_2) is False


@pytest.mark.parametrize(
    "price, quantity, expected_total",
    [
        (
            10.00,
            1,
            10.00,
        ),
        (
            7.50,
            3,
            22.50,
        ),
    ],
)
def test_subtotals(price, quantity, expected_total):
    product = Product(id=1, description="Goalie Gloves", price=price)
    item = Item(product=product, quantity=quantity)
    assert item.get_subtotal() == expected_total


@dataclass
class OrderTotalCase:
    products: list[Product]
    country: Country
    expected_total: float


@pytest.mark.parametrize(
    "order_total_case",
    [
        OrderTotalCase(
            products=[
                Product(id=1, description="Celtic Jersey", price=51.00),
                Product(id=2, description="Partick Jersey", price=51.00),
            ],
            country=Country.UNITED_KINGDOM,
            expected_total=102.00,
        ),
        OrderTotalCase(
            products=[
                Product(id=1, description="Celtic Jersey", price=51.00),
                Product(id=2, description="Partick Jersey", price=51.00),
            ],
            country=Country.FRANCE,
            expected_total=106.99,
        ),
        OrderTotalCase(
            products=[
                Product(id=1, description="Celtic Jersey", price=51.00),
                Product(id=2, description="Partick Jersey", price=51.00),
            ],
            country=Country.ARMENIA,
            expected_total=111.99,
        ),
        OrderTotalCase(
            products=[
                Product(id=1, description="Hibs Jersey", price=45.00),
            ],
            country=Country.UNITED_KINGDOM,
            expected_total=49.99,
        ),
        OrderTotalCase(
            products=[
                Product(id=1, description="Hibs Jersey", price=45.00),
            ],
            country=Country.FRANCE,
            expected_total=53.99,
        ),
        OrderTotalCase(
            products=[
                Product(id=1, description="Hibs Jersey", price=45.00),
            ],
            country=Country.ARMENIA,
            expected_total=54.99,
        ),
    ],
)
def test_order_total_with_shipping(order_total_case):
    order = (
        OrderBuilder(order_id="ORDER_1")
        .with_address(order_total_case.country)
        .with_products(order_total_case.products)
        .build()
    )
    assert order.get_total() == order_total_case.expected_total
