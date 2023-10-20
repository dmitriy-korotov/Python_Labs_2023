import datetime
from Product import Product


class FoodProduct(Product):

    def __init__(self, _title: str, _cost: int,  _width: int, _height: int, _length: int, _best_before_date: datetime):
        super().__init__(_title, _cost, _width, _height, _length)
        self.__best_before_date = _best_before_date

    def __str__(self) -> str:
        return super().__str__() + f"\nBest before date: {self.__best_before_date}"
