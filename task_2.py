class Ship:
    def __init__(self, name, length, max_speed):
        self.name = name
        self.length = length
        self.max_speed = max_speed
    
    def display_info(self):
        print(f"Ship Name: {self.name}")
        print(f"Length: {self.length} meters")
        print(f"Max Speed: {self.max_speed} knots")


class Frigate(Ship):
    def __init__(self, name, length, max_speed, num_missiles):
        super().__init__(name, length, max_speed)
        self.num_missiles = num_missiles
    
    def display_info(self):
        super().display_info()
        print(f"Number of Missiles: {self.num_missiles}")


class Destroyer(Ship):
    def __init__(self, name, length, max_speed, num_guns):
        super().__init__(name, length, max_speed)
        self.num_guns = num_guns
    
    def display_info(self):
        super().display_info()
        print(f"Number of Guns: {self.num_guns}")


class Cruiser(Ship):
    def __init__(self, name, length, max_speed, num_cannons):
        super().__init__(name, length, max_speed)
        self.num_cannons = num_cannons
    
    def display_info(self):
        super().display_info()
        print(f"Number of Cannons: {self.num_cannons}")



frigate = Frigate("Frigate1", 150, 30, 50)
frigate.display_info()

destroyer = Destroyer("Destroyer1", 200, 35, 80)
destroyer.display_info()

cruiser = Cruiser("Cruiser1", 250, 40, 100)
cruiser.display_info()
