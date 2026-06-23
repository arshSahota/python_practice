class Dog:
    def speak(self):
        return "woof"
    
class Cat:
    def speak(self):
        return "Meow"
    
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())