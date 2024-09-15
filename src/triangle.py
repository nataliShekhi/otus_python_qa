from figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")
        if side_a + side_b <= side_c or side_b + side_c <= side_a or side_c + side_a <= side_b:
            raise ValueError("Треугольник существует только тогда, когда сумма двух его сторон больше третьей")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @classmethod
    def create_triangle(cls, *args):
        if len(args) != 3:
            raise ValueError("Должны быть переданы все три стороны треугольника")
        return cls(*args)

    @property
    def area(self):
        half_perimetr = self.get_perimeter/2
        return math.sqrt(half_perimetr * (half_perimetr - self.side_a) * (half_perimetr - self.side_b) * (half_perimetr - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

