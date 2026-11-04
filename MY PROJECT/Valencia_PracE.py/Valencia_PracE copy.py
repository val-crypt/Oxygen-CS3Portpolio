class LabEquipment:
    def __init__(self, name, brand, magnification):
        self.name = name
        self.brand = brand
        self.magnification = magnification


    def display_info(self):
        print("===== MICROSCOPE =====")
        print(f"Name: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Magnification: {self.magnification}")
        print()

equipment1 = LabEquipment("Digital Microscope", "Leica", "1000x")



equipment1.display_info()

print("Viewing specimen in 1000x magnification using the Leica Digital Microscope.")
