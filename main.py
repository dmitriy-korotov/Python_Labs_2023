from HouseholdGood import HouseholdGood
from FoodProduct import FoodProduct
from Shop import Shop
import InputHandlers as Ih
import pickle
import os
from sys import stdout


def write_shop(_shop: Shop):
    with open("shop.txt", "ab") as file:
        pickle.dump(_shop, file)


def read_shop() -> Shop:
    with open("shop.txt", "rb") as file:
        return pickle.load(file)


def main():
    shop = Shop("BestShop")

    if os.path.exists("shop.txt"):
        try:
            shop = read_shop()
            shop.print_products()
        except pickle.PickleError as error:
            print(error)
        except Exception as ex:
            print(ex)

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
        shop.print_products()
        write_shop(shop)
    except pickle.PickleError as error:
        print(error)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
