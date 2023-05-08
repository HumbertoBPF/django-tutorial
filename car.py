class Car:
    def __init__(self, model, price, color, build_year):
        self.model = model
        self.price = price
        self.color = color
        self.build_year = build_year

    def is_popular(self):
        return self.price <= 25000

    def __str__(self):
        return str(self.model) + " - " + str(self.color) + " - " + str(self.build_year)


car1 = Car("AAA", 10000, "orange", 2015)
car2 = Car("BBB", 15000, "blue", 2018)
car3 = Car("CCC", 45000, "green", 2015)

print(car1)
print(car2)
print(car3)
