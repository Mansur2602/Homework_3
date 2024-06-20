class Square:
    def __init__(self, storona):
        self.сторона = storona

    def area(self):
        return self.сторона ** 2


class Radius(Square):
    def __init__(self, storona):
        super().__init__(storona)
        self.radius = storona / 2

    def area_radius(self):
        return 3.14159 * self.radius ** 2


a = Radius(10)
print("Площадь окружности, вписанной в квадрат:", a.area_radius())
print("Площадь квадрата:", a.area())
