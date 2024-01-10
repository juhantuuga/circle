import math


class Circle:
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            self.radius = 0

    def get_radius(self):
        return self.radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2  # kaks tärni on ruudus

    def __str__(self):
        return (f'raadius: {self.radius}, '
                f'diameeter: {self.get_diameter()}, '
                f'ümbermõõt: {self.get_perimeter()}, '
                f'pindala: {self.get_area()}')