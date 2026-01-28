class Car:
    base_price = 100000

    def __init__(self, windows, doors, power):
        self.windows = windows
        self.doors = doors
        self.power = power

    def what_base_price(self):
        print("The base price is:", Car.base_price)

    @classmethod
    def revise_base_price(cls, inflation):
        cls.base_price = cls.base_price + cls.base_price * inflation
        return cls.base_price

print(Car.revise_base_price(0.1))
print(Car.base_price)

# print(Car.revise_base_price(0.1)+Car.revise_base_price(0.07))
