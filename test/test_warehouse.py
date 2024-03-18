import pytest

from src.product import Product
from src.warehouse import Entry, Warehouse


@pytest.mark.parametrize("stock", [0, 1, 2, 3, 4, 10])
def test_check_stock(stock):
    product = Product(id=1, description="Celtic Jersey", price=50.00)
    entry = Entry(product=product, stock=stock)
    warehouse = Warehouse(catalogue=[entry])
    assert warehouse.check_stock(product) == stock
