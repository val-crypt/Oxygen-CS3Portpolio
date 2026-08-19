class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ₱{self.price}")
        print(f"Quantity: {self.quantity}")

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"{quantity} {self.name} sold.")
            print(f"New quantity: {self.quantity}")
        else:
            print("Not enough stock.")

    def restock(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.quantity = amount
            print(f"Restocked {amount} item(s).")
            print(f"New quantity: {self.quantity}")


def demo():
    products = [
        Product("Lucky Me Pancit Canton", 15, 20),
        Product("Coca-Cola", 25, 15),
        Product("SkyFlakes", 10, 30),
        Product("Piattos", 25, 12),
        Product("Sardines", 30, 10),
    ]

    for p in products:
        p.display_info()
        print(" -- " * 10)

    # demonstrate restock and sell on first product
    first = products[0]
    print(" --- Restocking 10 items ---")
    first.restock(10)
    print(" --- Selling 5 items ---")
    first.sell(5)
    first.display_info()


if __name__ == "__main__":
    demo()