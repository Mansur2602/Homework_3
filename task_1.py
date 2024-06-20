class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def turn_on(self):
        print(f"{self.brand} {self.model} включен")

    def turn_off(self):
        print(f"{self.brand} {self.model} выключен")


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_capacity):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity

    def make_coffee(self):
        print(f"Приготовление кофе на кофемашине {self.brand} {self.model}")


class Blender(Device):
    def __init__(self, brand, model, power, speed_levels):
        super().__init__(brand, model, power)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"Использование блендера {self.brand} {self.model} для приготовления блюд")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, blades):
        super().__init__(brand, model, power)
        self.blades = blades

    def grind_meat(self):
        print(f"Использование мясорубки {self.brand} {self.model} для измельчения мяса")



coffee_machine = CoffeeMachine("Philips", "HD7450", 850, 1.5)
blender = Blender("Braun", "JB3060", 700, 5)
meat_grinder = MeatGrinder("Moulinex", "ME625", 1000, 4)

coffee_machine.turn_on()
coffee_machine.make_coffee()
coffee_machine.turn_off()

blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.turn_off()






