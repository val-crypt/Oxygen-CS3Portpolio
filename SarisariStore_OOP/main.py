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


# ---------- MENU FEATURE ADDED BELOW ----------

products = [
    Product("Lucky Me Pancit Canton", 15, 20),
    Product("Coca-Cola", 25, 15),
    Product("SkyFlakes", 10, 30),
    Product("Piattos", 25, 12),
    Product("Sardines", 30, 10),
]


def show_all_products():
    for p in products:
        p.display_info()
        print(" -- " * 10)


def search_product():
    name = input("Enter product name to search: ").strip().lower()
    for p in products:
        if p.name.lower() == name:
            p.display_info()
            return


# ---------- CHALLENGE 2: SHOPPING CART ----------

class ShoppingCart:
    def __init__(self):
        # each entry: {"product": Product, "quantity": int}
        self.items = []

    def add_item(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity > product.quantity:
            print(f"Not enough stock. Only {product.quantity} {product.name} left.")
            return

        # If the product is already in the cart, just increase the quantity
        for entry in self.items:
            if entry["product"] is product:
                entry["quantity"] += quantity
                print(f"Updated {product.name} quantity in cart to {entry['quantity']}.")
                return

        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity} {product.name} to cart.")

    def remove_item(self, product_name):
        product_name = product_name.strip().lower()
        for entry in self.items:
            if entry["product"].name.lower() == product_name:
                self.items.remove(entry)
                print(f"Removed {entry['product'].name} from cart.")
                return
        print("Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("\n----- YOUR CART -----")
        for entry in self.items:
            product = entry["product"]
            qty = entry["quantity"]
            subtotal = product.price * qty
            print(f"{product.name} x{qty} = ₱{subtotal}")
        print(f"TOTAL: ₱{self.get_total()}")
        print("----------------------\n")

    def get_total(self):
        return sum(entry["product"].price * entry["quantity"] for entry in self.items)

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Nothing to check out.")
            return

        print("\n----- RECEIPT -----")
        for entry in self.items:
            product = entry["product"]
            qty = entry["quantity"]
            product.sell(qty)  # deducts from actual stock
        print(f"TOTAL PAID: ₱{self.get_total()}")
        print("Thank you for shopping!")
        print("--------------------\n")

        self.items = []  # empty the cart after checkout


def find_product_by_name(name):
    name = name.strip().lower()
    for p in products:
        if p.name.lower() == name:
            return p
    return None


# ---------- MAIN MENU LOOP ----------

def main():
    cart = ShoppingCart()

    while True:
        print("\n===== SARI-SARI STORE =====")
        print("1. View all products")
        print("2. Search product")
        print("3. Add item to cart")
        print("4. View cart")
        print("5. Remove item from cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_all_products()

        elif choice == "2":
            search_product()

        elif choice == "3":
            name = input("Enter product name to add: ")
            product = find_product_by_name(name)
            if product is None:
                print("Product not found.")
                continue
            try:
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            cart.add_item(product, qty)

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            name = input("Enter product name to remove: ")
            cart.remove_item(name)

        elif choice == "6":
            cart.checkout()

        elif choice == "7":
            print("Thank you for visiting the Sari-Sari Store!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()