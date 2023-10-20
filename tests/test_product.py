import pytest
from .. import Product.Product


class ProductTest:
    def __init__(self):
        pass

    @pytest.fixture
    def product(self):
        return Product("Product", 50, 4, 5, 10)

    @pytest.mark.parametrize("box_size, expected", [[(10, 10, 10), 5], [(1, 1, 1), 0], [(10, 15, 5), 3]])
    def test_get_number_of_products_that_fit_in_box(self, product, box_size, expected):
        assert product.get_number_of_products_that_fit_in_box(box_size[0], box_size[1], box_size[2]) == expected
