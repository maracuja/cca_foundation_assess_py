from dataclasses import dataclass
import pytest

from src.product import Product
from src.warehouse import Entry, Warehouse, InsufficientStockError, ProductNotFoundError
from test.builders import AddressBuilder, OrderBuilder


@pytest.mark.parametrize("stock", [0, 1, 2, 3, 4, 10])
def test_check_stock(stock):
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=stock)
    warehouse = Warehouse(catalogue={1: entry})
    assert warehouse.check_stock(product) == stock


@dataclass
class StockCheckCase:
    initial: int
    adjustment: int
    expected: int


@pytest.mark.parametrize(
    "stock_check_case",
    [
        StockCheckCase(initial=1, adjustment=1, expected=0),
        StockCheckCase(initial=3, adjustment=2, expected=1),
    ],
)
def test_adjust_stock(stock_check_case):
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=stock_check_case.initial)
    warehouse = Warehouse(catalogue={1: entry})
    warehouse.adjust_stock(product, stock_check_case.adjustment)
    assert warehouse.check_stock(product) == stock_check_case.expected


def test_not_enough_stock():
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=10)
    warehouse = Warehouse(catalogue={1: entry})
    with pytest.raises(InsufficientStockError):
        warehouse.adjust_stock(product, 11)


@pytest.mark.parametrize(
    "stock_check_case",
    [
        StockCheckCase(initial=0, adjustment=0, expected=0),
        StockCheckCase(initial=1, adjustment=1, expected=2),
        StockCheckCase(initial=3, adjustment=2, expected=5),
    ],
)
def test_receive_stock(stock_check_case):
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=stock_check_case.initial)
    warehouse = Warehouse(catalogue={1: entry})
    warehouse.receive_stock(product, stock_check_case.adjustment)
    assert warehouse.check_stock(product) == stock_check_case.expected


def test_add_already_in_warehouse_product():
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=1)
    warehouse = Warehouse(catalogue={1: entry})
    warehouse.add_entry(entry)
    assert warehouse.check_stock(product) == 2


def test_product_not_found():
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=1)
    warehouse = Warehouse(catalogue={1: entry})
    with pytest.raises(ProductNotFoundError):
        warehouse.get_entry(Product(id=2, description="Rangers Trophy", price=10.00))


def test_order_confirmed():
    products = [
        Product(id=1, description="Celtic Jersey", price=50.00),
        Product(id=2, description="Hibs Jersey", price=40.00),
        Product(id=3, description="Partick Jersey", price=40.00),
    ]
    warehouse = Warehouse(catalogue={})
    for product in products:
        warehouse.add_entry(Entry(product=product, stock=20))

    order = OrderBuilder(order_id="ORDER_1").with_products(products).build()
    warehouse.confirm_order(order)

    assert len(warehouse.sales_history.orders) == 1
    assert (
        len(
            warehouse.sales_history.get_orders_by_address(
                AddressBuilder(address_id="ADDRESS_1").build()
            )
        )
        == 1
    )
    for product in products:
        assert warehouse.check_stock(product) == 19
