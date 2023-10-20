from HouseholdGood import HouseholdGood
from FoodProduct import FoodProduct


def main():
    prod = HouseholdGood("Title", 500, 10, 10, 10, 5)
    print(prod)

    try:
        title = input("Input title: ")
        cost = int(input("Input cost: "))
        width = int(input("Input width: "))
        height = int(input("Input height: "))
        length = int(input("Input length: "))
        date = input("Input date: ")

        food_prod = FoodProduct(title, cost, width, height, length, date)
    except ValueError:
        print("Incorrect data.")


if __name__ == "__main__":
    main()

