class Vehicle:
    def __init__(self, wheels, capacity, model, price, color, build_year):
        self.wheels = wheels
        self.capacity = capacity
        self.model = model
        self.price = price
        self.color = color
        self.build_year = build_year


class Car(Vehicle):
    def __init__(self, model, price, color, build_year):
        super().__init__(4, 5, model, price, color, build_year)

    def is_popular(self):
        return self.price <= 25000


car1 = Car("AAA", 10000, "orange", 2015)
car2 = Car("BBB", 15000, "blue", 2018)
car3 = Car("CCC", 45000, "green", 2015)

print(car1.is_popular())
print(car2.is_popular())
print(car3.is_popular())
