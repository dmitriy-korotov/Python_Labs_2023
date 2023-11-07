import pytest

from HouseholdGood import HouseholdGood
from Product import Product
from Shop import Shop
from main import write_and_read_shop


class TestProduct:

    @pytest.fixture
    def product(self):
        return Product("Product", 50, 4, 5, 10)

    @pytest.mark.parametrize("box_size, expected", [[(10, 10, 10), 5], [(1, 1, 1), 0], [(10, 15, 5), 3]])
    def test_get_number_of_products_that_fit_in_box(self, product, box_size, expected):
        assert product.get_number_of_products_that_fit_in_box(box_size[0], box_size[1], box_size[2]) == expected

    @pytest.mark.parametrize("expected", ["Product"])
    def test_get_title(self, product, expected):
        assert product.get_title() == expected

    def test_shop_dumping(self):
        shop = Shop("Shop")
        shop.add_product(HouseholdGood("Product", 10, 20, 30, 40, 5))
        shop = write_and_read_shop(shop)
        product = shop.get_products()[0]

        assert product.get_title() == "Product"
        assert product.get_cost() == 10
        assert product.get_width() == 20
        assert product.get_height() == 30
        assert product.get_length() == 40
        assert product.get_quality() == 5
