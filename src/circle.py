from figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус круга не может быть меньше 0")
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius