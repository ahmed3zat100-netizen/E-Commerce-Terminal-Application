
#main


from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from cart import ShoppingCart


#Products
products = [

    PhysicalProduct(1, "Laptop", 1000, 5, 50),
    PhysicalProduct(2, "Phone", 700, 10, 30),

    DigitalProduct(3, "Python Course", 200, 100, 1500),
    DigitalProduct(4, "Ebook", 100, 50, 20)
]

#Cart
cart = ShoppingCart()


def view_products():

    print("\n===== Products =====")

    for product in products:
        product.display_info()


def add_to_cart():

    try:
        product_id = int(input("Enter Product ID: "))

        found = False

        for product in products:

            if product.get_id() == product_id:

                if product.get_stock() > 0:

                    cart.add_product(product)

                    # reduce stock
                    product.set_stock(product.get_stock() - 1)

                else:
                    print("Out of stock!")

                found = True
                break

        if not found:
            print("Product not found!")

    except ValueError:
        print("Please enter a valid number!")


while True:

    print("\n========== E-Commerce System ==========")
    print("1. View Products")
    print("2. Add To Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            cart.view_cart()

        elif choice == 4:
            cart.checkout()

        elif choice == 5:
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a number only!")