from Product import Product


class HouseholdGood(Product):

    def __init__(self, _title: str, _cost: int, _width: int, _height: int, _length: int, _quality: int):  # quality: from 0 to 10
        super().__init__(_title, _cost, _width, _height, _length)
        if _quality < 0 or _quality > 10:
            raise Exception("Quality must be in interval [0, 10]")
        self.__quality = _quality

    def __str__(self) -> str:
        return super().__str__() + f"\nQuality: {self.__quality}"

    def sell(self, _sold_cost: int) -> None:
        print(f"The household product is sold (price: {self.__cost}, sold cost: {_sold_cost}).")
