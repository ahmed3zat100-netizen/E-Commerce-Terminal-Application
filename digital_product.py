
# digital_product


from product import Product


class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, file_size):
        super().__init__(product_id, name, price, stock)
        self.file_size = file_size

    def apply_discount(self):
        #20%discount
        return self.get_price() * 0.8

    def display_info(self):
        print(f"[{self.get_id()}] {self.get_name()} "
              f"- Price: {self.get_price()} "
              f"- File Size: {self.file_size}MB")