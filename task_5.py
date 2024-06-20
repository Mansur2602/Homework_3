import pickle

class Shape:
    def __init__(self):
        pass

    def Show(self):
        pass

    def Save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def Load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def Show(self):
        print(f"Square at ({self.x}, {self.y}) with side length {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def Show(self):
        print(f"Circle at ({self.x}, {self.y}) with radius {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Ellipse at ({self.x}, {self.y}) with width {self.width} and height {self.height}")


shapes = [
    Square(0, 0, 5),
    Rectangle(2, 3, 4, 6),
    Circle(1, 1, 3),
    Ellipse(5, 5, 4, 2)
]


for i, shape in enumerate(shapes):
    shape.Save(f'shape_{i}.txt')


loaded_shapes = []
for i in range(len(shapes)):
    loaded_shapes.append(Shape.Load(f'shape_{i}.txt'))


for shape in loaded_shapes:
    shape.Show()
