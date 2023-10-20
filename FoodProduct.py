import datetime
from Product import Product


class FoodProduct(Product):

    def __init__(self, _title: str, _cost: int,  _width: int, _height: int, _length: int, _best_before_date: str):
        super().__init__(_title, _cost, _width, _height, _length)
        try:
            self.__best_before_date = datetime.date.fromisoformat(_best_before_date)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        print("FoodProduct created.")

    def __str__(self) -> str:
        return super().__str__() + f"\nBest before date: {self.__best_before_date.__str__()}"
