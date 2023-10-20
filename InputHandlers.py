import datetime
from HouseholdGood import HouseholdGood
from FoodProduct import FoodProduct


def input_int(_left_bound: int, _right_bound: int, _input_msg: str):
    num = input(_input_msg + ":\t")

    while True:

        try:
            int_num = int(num)
        except Exception as ex:
            print("Can't cast to integer type, please retry")
        else:
            if _left_bound <= int_num <= _right_bound:
                break
            else:
                print(f"Please input value from {_left_bound} to {_right_bound}")

        num = input(_input_msg + ":\t")

    return int_num


def input_date(_input_msg: str):
    str_date = input(_input_msg + ":\t")

    while True:

        try:
            date = datetime.date.fromisoformat(str_date)
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
        else:
            break

        str_date = input(_input_msg + ":\t")

    return date


def input_household_good():

    print("Fill household good product data:\n")

    title = input("Input product title:\t")
    cost = input_int(0, 10000, "Input product cost")
    width = input_int(0, 100, "Input product width")
    height = input_int(0, 100, "Input product height")
    length = input_int(0, 100, "Input product length")
    quality = input_int(0, 10, "Input product quality")

    return HouseholdGood(title, cost, width, height, length, quality)


def input_food_product():

    print("Fill food product data:\n")

    title = input("Input product title:\t")
    cost = input_int(0, 10000, "Input product cost")
    width = input_int(0, 100, "Input product width")
    height = input_int(0, 100, "Input product height")
    length = input_int(0, 100, "Input product length")
    date = input_date("Input product best before date")

    return FoodProduct(title, cost, width, height, length, date)
