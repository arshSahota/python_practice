class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * 3.14 * 2

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
shapes = [Circle(2), Rectangle(1,2)]

for shape in shapes:
    print(shape.area())
        