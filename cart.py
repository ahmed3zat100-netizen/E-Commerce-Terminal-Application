
#cart


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.get_name()} added to cart.")

    def view_cart(self):

        if not self.items:
            print("Cart is empty.")
            return

        print("\n===== Shopping Cart =====")

        for item in self.items:
            item.display_info()

    def checkout(self):

        if not self.items:
            print("Cart is empty.")
            return

        total = 0

        print("\n===== Checkout =====")

        for item in self.items:
            final_price = item.apply_discount()

            print(f"{item.get_name()} -> Final Price: {final_price}")

            total += final_price

        print(f"\nTotal Price = {total}")