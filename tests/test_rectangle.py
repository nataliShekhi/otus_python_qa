import pytest
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle


@pytest.mark.parametrize(
    "side_a,side_b,area", [(3, 5, 15), (3.5, 5.5, 19.25)], ids=["integer", "float"]
)
@pytest.mark.smoke
@pytest.mark.rectangle
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f"Площадь для чисел {side_a} и {side_b} должна быть {area}"


@pytest.mark.parametrize(
    "side_a,side_b,perimeter", [(3, 5, 16), (3.5, 5.5, 18)], ids=["integer", "float"]
)
@pytest.mark.smoke
@pytest.mark.rectangle
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert (
        r.perimeter == perimeter
    ), f"Периметр для чисел {side_a} и {side_b} должен быть равен {perimeter}"


@pytest.mark.parametrize(
    "side_a,side_b", [(-3, 5), (3, -5), (-3, -5)], ids=["negative side_a", "negative side_b", "negative side_a and "
                                                                                              "side_b"]
)
@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.rectangle
def test_rectangle_incorrect_values(side_a, side_b):
    r = Rectangle(side_a, side_b)
    assert (
        r.side_a <= 0 or r.side_b <= 0
    ), f"Стороны прямоугольника не могут равны или меньше 0"


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        (Rectangle(2, 5), Triangle(4, 3, 6), 10 + 5.33),
        (Rectangle(2, 5), Square(3), 10 + 9),
        (Rectangle(2, 5), Rectangle(4, 3), 10 + 12),
        (Rectangle(2, 5), Circle(2), 10 + 12.56),
    ],
    ids=["triangle+rectangle", "square+rectangle", "rectangle+rectangle", "rectangle+circle"]
)
@pytest.mark.smoke
@pytest.mark.rectangle
@pytest.mark.positive
def test_add_area_positive(figure1, figure2, expected_area):
    assert figure1.add_area(figure2) == pytest.approx(expected_area, rel=1e-2), \
        (f"Сумма площадей двух фигур просчитана корректно")


@pytest.mark.parametrize(
    "figure1, figure2",
    [
        (Rectangle(2, 5), 10),
    ],
    ids=["rectangle + not a figure"]
)
@pytest.mark.rectangle
@pytest.mark.negative
def test_add_area_not_figure(figure1, figure2):
    with pytest.raises(ValueError, match="В метод add_area передана не геометрическая фигура"):
        figure1.add_area(figure2)