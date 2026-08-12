from pathlib import Path

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def display(self):
        return f"{self.name} - ${self.total_price()}"

    def increase_quantity(self, amount):
        self.quantity += amount

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def get_total(self):
        return sum(product.total_price() for product in self.cart)

    def remove_product(self, name):
        for product in self.cart:
            if product.name == name:
                self.cart.remove(product)
                break

    def show_cart(self):
        print("Shopping Cart:")
        print()
        for product in self.cart:
            print(product.display())
        print()
        print(f"Total: {self.get_total()}")

    def save_cart(self, filename):
        path = Path(filename)

        contents = ''

        for product in self.cart:
            contents += f"{product.name}, {product.price}, {product.quantity}\n"

        path.write_text(contents, encoding="utf-8")
        print("Cart saved.")

    def load_cart(self, filename):
        path = Path(filename)
        try:
            contents = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print("File not found.")
        else:
            lines = contents.splitlines()

            for line in lines:
                name, price, quantity = line.split(",")

                product = Product(name, int(price), int(quantity))

                self.cart.append(product)


apple = Product("Apple", 3, 5)
banana = Product("Banana", 2, 10)

cart = ShoppingCart()

cart.add_product(apple)
cart.add_product(banana)

cart.show_cart()

print(cart.get_total())

apple.increase_quantity(3)

cart.show_cart()

print(cart.get_total())
