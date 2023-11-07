from Product import Product


class Shop(object):

    def __init__(self, _title: str):
        self.__title = _title
        self.__products = []

    def add_product(self, _product: Product):
        self.__products.append(_product)

    def remove_product(self, _title: str):
        self.__products.remove(self.__products.index(lambda x: x.get_title() == _title))

    def get_products(self):
        return self.__products

    def get_products_count(self):
        return len(self.__products)

    def save_to_file(self, _filename: str):
        pass

    def print_products(self):
        print("\t\tProducts:")
        for product in self.get_products():
            print(f"\n\n{product}\n\n")
