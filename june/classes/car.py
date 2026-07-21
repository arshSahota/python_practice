from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors


car = Car("BMW", 4)

print(car.brand)
print(car.doors)