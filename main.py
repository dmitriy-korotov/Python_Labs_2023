from HouseholdGood import HouseholdGood
from FoodProduct import FoodProduct
from Shop import Shop
import InputHandlers as Ih


def main():

    shop = Shop("BestShop")

    product = Ih.input_food_product()
    shop.add_product(shop)

    shop.print_products()


if __name__ == "__main__":
    main()

