class Car:
    def __init__(self, wheel_count, engine_power, door_count):
        self.wheel_count = wheel_count
        self.engine_power = engine_power
        self.door_count = door_count

    def car_info(self):
        return f"The car has {self.wheel_count} wheels, engine power of {self.engine_power} hp, and {self.door_count} doors"


class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def wheels_info(self):
        return f"The car has {self.wheel_count} wheels"


class Engine:
    def __init__(self, engine_power):
        self.engine_power = engine_power

    def engine_info(self):
        return f"Engine power: {self.engine_power} hp"


class Doors:
    def __init__(self, door_count):
        self.door_count = door_count

    def doors_info(self):
        return f"The car has {self.door_count} doors"


class CarWithFeatures(Car, Wheels, Engine, Doors):
    def __init__(self, wheel_count, engine_power, door_count):
        Car.__init__(self, wheel_count, engine_power, door_count)
        Wheels.__init__(self, wheel_count)
        Engine.__init__(self, engine_power)
        Doors.__init__(self, door_count)


car = CarWithFeatures(4, 200, 2)
print(car.car_info())
