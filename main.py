from HouseholdGood import HouseholdGood
from FoodProduct import FoodProduct
from Shop import Shop
import InputHandlers as Ih
import pickle
from sys import stdout


def write_and_read_shop(_shop: Shop):
    with open("shop.txt", "wb") as file:
        pickle.dump(_shop, file)

    with open("shop.txt", "rb") as file:
        return pickle.load(file)


def main():
    shop = Shop("BestShop")

    is_need_input = True
    while is_need_input:

        product_type = input("Select product type (F or H):\t")

        if product_type == "F":
            product = Ih.input_food_product()
        elif product_type == "H":
            product = Ih.input_household_good()
        else:
            continue

        shop.add_product(product)

        is_need_break = input("If you want end input press F")
        if is_need_break.lower() == "f":
            break

    try:
        shop = write_and_read_shop(shop)
        shop.print_products()
    except pickle.PickleError as error:
        print(error)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
