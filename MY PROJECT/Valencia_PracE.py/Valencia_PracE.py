class SmartLocker:
    def __init__(self, locker_number, owner=None, status="Available"):
        self.locker_number = locker_number
        self.owner = owner
        self.status = status

    def assign_locker(self, name):
        self.owner = name
        self.status = "Occupied"

    def release_locker(self):
        self.owner = None
        self.status = "Available"

    def display_info(self):
        print("===== Smart Locker Information =====")
        print(f"Locker Number: {self.locker_number}")
        print(f"Owner: {self.owner}")
        print(f"Status: {self.status}")
        print()

locker101 = SmartLocker(101)
locker102 = SmartLocker(102)

locker101.assign_locker("EJ")
locker102.assign_locker("UNO")

locker101.display_info()
locker102.display_info()

locker101.release_locker()

print("===== After Releasing Locker 101 =====")
locker101.display_info()
locker102.display_info()

print("===== New Status =====")
print(f"Locker 101 status: {locker101.status}")
print(f"Locker 102 status: {locker102.status}")