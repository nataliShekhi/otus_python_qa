import pytest
from triangle import Triangle
from circle import Circle


@pytest.mark.parametrize(
    "side_a,side_b,side_c,area",
    [(3, 4, 5, 6), (3.5, 4.5, 5.5, 7.854885024620029)],
    ids=["integer", "float"],
)
@pytest.mark.smoke
@pytest.mark.triangle
def test_triangle_area_positive(side_a, side_b, side_c, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.area == area, f"Площадь должна быть {area}"


@pytest.mark.parametrize(
    "side_a,side_b,side_c,area",
    [(3, 4, 5, 5), (3.5, 4.5, 5.5, 5.854885024620029)],
    ids=["integer", "float"],
)
@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_area_negative(side_a, side_b, side_c, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.area != area, f"Площадь рассчитана некорректно"


@pytest.mark.parametrize(
    "side_a,side_b,side_c,perimeter",
    [(3, 4, 5, 12), (3.5, 4.5, 5.5, 13.5)],
    ids=["integer", "float"],
)
@pytest.mark.smoke
@pytest.mark.triangle
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"


@pytest.mark.parametrize(
    "side_a,side_b,side_c,perimeter",
    [(3, 4, 5, 11), (3.5, 4.5, 5.5, 13)],
    ids=["integer", "float"],
)
@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_perimeter_negative(side_a, side_b, side_c, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.perimeter != perimeter, f"Периметр рассчитан некорректно"


@pytest.mark.parametrize(
    "side_a,side_b,side_c",
    [(-3, 4, 5), (3, -4, 5), (3, 4, -5), (0, 0, 0)],
    ids=["negative side_a", "negative side_b", "negative side_c", "values 0"],
)
@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_incorrect_values(side_a, side_b, side_c):
    r = Triangle(side_a, side_b, side_c)
    assert r.side_a <= 0 or r.side_b <= 0 or r.side_c <= 0, f"Стороны треугольника должны быть больше 0"


@pytest.mark.parametrize(
    "side_a,side_b,side_c",
    [(2, 1, 5), (5, 2, 3), (3, 8, 4)],
    ids=["side_a + side_b <= side_c", "side_b + side_c <= side_a", "side_c + side_a <= side_b"],
)
@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_sum_of_the_sides(side_a, side_b, side_c):
    r = Triangle(side_a, side_b, side_c)
    assert r.side_a + r.side_b <= r.side_c or r.side_b + r.side_c <= r.side_a or r.side_c + r.side_a <= r.side_b, \
        f"Треугольник существует только тогда, когда сумма двух его сторон больше третьей"


@pytest.mark.parametrize(
    "side_a,side_b,side_c",
    [(5, None, None), (None, 2, None), (3, 8, None)],
    ids=["only 1 side", "side_b is none", "only 2 sides"],
)
@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_three_sides(side_a, side_b, side_c):
    r = Triangle(side_a, side_b, side_c)
    assert r.side_a is None or r.side_b is None or r.side_c is None, f"Должны быть переданы все три стороны треугольника"


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        (Triangle(4, 3, 6), Triangle(4, 3, 6), 5.3326822519 + 5.3326822519),
        (Triangle(4, 3, 6), Circle(2), 5.3326822519 + 12.566370614359172),
    ],
    ids=["triangle+triangle", "triangle+circle"]
)
@pytest.mark.smoke
@pytest.mark.triangle
@pytest.mark.positive
def test_add_area_positive(figure1, figure2, expected_area):
    assert figure1.add_area(figure2) == pytest.approx(expected_area), \
        (f"Сумма площадей двух фигур просчитана корректно")


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        (Triangle(4, 3, 6), Triangle(4, 3, 6), 6 + 5.3326822519),
        (Triangle(4, 3, 6), Circle(2), 5.3326822519 + 15),
    ],
    ids=["triangle+triangle", "triangle+circle"]
)
@pytest.mark.triangle
@pytest.mark.negative
def test_add_area_negative(figure1, figure2, expected_area):
    assert figure1.add_area(figure2) != pytest.approx(expected_area), \
        (f"Сумма площадей двух фигур просчитана некорректно")


@pytest.mark.parametrize(
    "figure1, figure2",
    [
        (Triangle(3, 4, 5), 10),
    ],
    ids=["triangle + not a figure"]
)
@pytest.mark.triangle
@pytest.mark.negative
def test_add_area_not_figure(figure1, figure2):
    with pytest.raises(ValueError, match="В метод add_area передана не геометрическая фигура"):
        figure1.add_area(figure2)