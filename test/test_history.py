from src.history import SalesHistory
from src.countries import Country
from test.builders import OrderBuilder


def test_add_order_to_sales_history():
    order = (
        OrderBuilder(order_id="ORDER_1").with_address(Country.UNITED_KINGDOM).build()
    )
    sales_history = SalesHistory()
    sales_history.add_order(order)

    assert len(sales_history.orders) == 1
