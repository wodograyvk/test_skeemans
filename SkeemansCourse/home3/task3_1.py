class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        print(f'Vehicle {self.brand} is moving with max speed {self.max_speed}!')

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    @property
    def max_speed_squared(self):
        return self.max_speed ** 2


class Bus(Vehicle):

    def move(self):
        return f'Bus {self.brand} is moving!'


if __name__ == '__main__':
    Audi_A4 = Vehicle("Audi_A4", 2014, 280)
    Audi_A4.move()

    Mersedes = Vehicle("Mersedes", 2008, 195)

    Mersedes.set_max_speed(70)
    print(Mersedes.max_speed_squared)

    Dodge = Vehicle("Dodge", 2012, 210)

    some_bus = Bus('Mersedes', 2008, 70)

    Audi_A4.move()
    Mersedes.move()
    Dodge.move()
    some_bus.move()

