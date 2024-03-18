from dataclasses import dataclass
import pytest

from src.product import Product
from src.warehouse import Entry, Warehouse, InsufficientStockError


@pytest.mark.parametrize("stock", [0, 1, 2, 3, 4, 10])
def test_check_stock(stock):
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=stock)
    warehouse = Warehouse(catalogue=[entry])
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
    warehouse = Warehouse(catalogue=[entry])
    warehouse.adjust_stock(product, stock_check_case.adjustment)
    assert warehouse.check_stock(product) == stock_check_case.expected


def test_not_enough_stock():
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=10)
    warehouse = Warehouse(catalogue=[entry])
    with pytest.raises(InsufficientStockError):
        warehouse.adjust_stock(product, 11)
