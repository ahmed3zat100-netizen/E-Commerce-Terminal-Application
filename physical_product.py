
# physical_product


from product import Product


class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, stock, shipping_cost):
        super().__init__(product_id, name, price, stock)
        self.shipping_cost = shipping_cost

    def apply_discount(self):
        #10% discount + shipping
        return (self.get_price() * 0.9) + self.shipping_cost

    def display_info(self):
        print(f"[{self.get_id()}] {self.get_name()} "
              f"- Price: {self.get_price()} "
              f"- Shipping: {self.shipping_cost}")