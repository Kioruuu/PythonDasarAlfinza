class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive!")

class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Flyyy!")

car1 = car("Skyline", "Gtr R34")
boat1 = boat("Ibiza", "Touring 20")
plane1 = plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
