class Equipment:
    def __init__(self, brand):
        self.brand = brand
        self.__status = "OFF"

    def use(self):
        self.__status = "ON"
        print("Equipment is now ON.")

    def get_status(self) -> str:
        return self.__status

# Step 5: Create an object
equipment1 = Equipment("Samsung")

# Step 6: Display the information
print(f"Brand: {equipment1.brand}")
print(f"Status: {equipment1.get_status()}")
equipment1.use()
print(f"Status: {equipment1.get_status()}")