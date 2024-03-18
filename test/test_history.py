from dataclasses import dataclass
from typing import Union
import pytest

from src.address import Address
from src.history import SalesHistory
from src.product import Product
from src.order import Order
from test.builders import OrderBuilder


def test_add_order_to_sales_history():
    order = OrderBuilder(order_id="ORDER_1").build()
    sales_history = SalesHistory()
    sales_history.add_order(order)

    assert len(sales_history.orders) == 1


@dataclass
class SalesHistoryCase:
    orders: list[Order]
    filter_by: Union[Product | Address]
    expected_order_ids: list[str]


TEST_PRODUCT_1 = Product(id=1, description="test 1", price=10.00)
TEST_PRODUCT_2 = Product(id=2, description="test 2", price=11.00)


@pytest.mark.parametrize(
    "sales_history_case",
    [
        SalesHistoryCase(
            orders=[
                OrderBuilder(order_id="ORDER_1")
                .with_products([TEST_PRODUCT_1])
                .build(),
                OrderBuilder(order_id="ORDER_2")
                .with_products([TEST_PRODUCT_2])
                .build(),
                OrderBuilder(order_id="ORDER_3")
                .with_products([TEST_PRODUCT_1, TEST_PRODUCT_2])
                .build(),
                OrderBuilder(order_id="ORDER_4").build(),
            ],
            filter_by=TEST_PRODUCT_1,
            expected_order_ids=["ORDER_1", "ORDER_3"],
        ),
        SalesHistoryCase(
            orders=[
                OrderBuilder(order_id="ORDER_1")
                .with_products([TEST_PRODUCT_1])
                .build(),
                OrderBuilder(order_id="ORDER_2")
                .with_products([TEST_PRODUCT_2])
                .build(),
                OrderBuilder(order_id="ORDER_3").build(),
                OrderBuilder(order_id="ORDER_4")
                .with_products([TEST_PRODUCT_1, TEST_PRODUCT_2])
                .build(),
            ],
            filter_by=TEST_PRODUCT_2,
            expected_order_ids=["ORDER_2", "ORDER_4"],
        ),
    ],
)
def test_sales_history_filters_by_product(sales_history_case):
    sales_history = SalesHistory()
    for order in sales_history_case.orders:
        sales_history.add_order(order)
    assert sales_history_case.expected_order_ids == [
        order.order_id
        for order in sales_history.get_orders_by_product(sales_history_case.filter_by)
    ]
