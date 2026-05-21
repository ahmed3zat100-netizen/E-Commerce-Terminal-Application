
#product


from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    #Getters
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    #Setters with validation
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative!")

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("Stock cannot be negative!")

    @abstractmethod
    def apply_discount(self):
        pass

    @abstractmethod
    def display_info(self):
        pass