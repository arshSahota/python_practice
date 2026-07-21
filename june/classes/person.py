class Person:
    population = 1

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def how_many(cls):
        return cls.population


