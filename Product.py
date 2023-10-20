class Product(object):

    def __init__(self, _title: str, _cost: int, _width: int, _height: int, _length: int):
        if _title == "":
            raise Exception("Title can't be empty.")
        self.__title = _title
        if _cost < 1:
            raise Exception("Minimal cost is one kopeck.")
        if _width < 1 or _height < 1 or _length < 1:
            raise Exception("Minimal size is one 'm'.")
        self.__cost = _cost
        self.__width = _width
        self.__height = _height
        self.__length = _length

    def get_title(self) -> str:
        return self.__title

    def get_cost(self) -> int:
        return self.__cost

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def get_length(self) -> int:
        return self.__length

    def get_number_of_products_that_fit_in_box(self, _box_with: int, _box_height: int, _box_length: int) -> int:
        v_product = self.__width * self.__height * self.__length
        v_box = _box_with * _box_height * _box_length
        return v_box // v_product

    def __add__(self, _other) -> int:
        v_this_product = self.__width * self.__height * self.__length
        v_other_product = other.__width * other.__height * other.__length
        return v_this_product * v_other_product

    def __str__(self) -> str:
        return f"""Title: {self.__title}\nCost: {self.__cost}\nWidth: {self.__width}\nHeight: {self.__height}\nLength: {self.__length}"""

    def sell(self) -> None:
        print(f"The product is sold (price: {self.__cost}).")
