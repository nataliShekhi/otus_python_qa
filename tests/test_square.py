import pytest
from square import Square
from circle import Circle
from triangle import Triangle


@pytest.mark.parametrize(
    "side_a, area", [(4, 16), (3.5, 12.25)], ids=["integer", "float"]
)
@pytest.mark.smoke
@pytest.mark.square
@pytest.mark.positive
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == area, f"Площадь должна быть {area}"


@pytest.mark.parametrize(
    "side_a, perimeter", [(4, 16), (3.5, 14)], ids=["integer", "float"]
)
@pytest.mark.smoke
@pytest.mark.square
@pytest.mark.positive
def test_square_perimeter_positive(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"


@pytest.mark.parametrize(
    "side_a, perimeter", [(-2, 8)], ids=["integer"]
)
@pytest.mark.smoke
@pytest.mark.square
@pytest.mark.negative
def test_square_incorrect_values(side_a, perimeter):
    s = Square(side_a)
    assert s.side_a <= 0, f"Сторона квадрата не может быть равна или меньше 0"


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        (Square(3), Triangle(4, 3, 6), 9 + 5.33),
        (Square(3), Circle(2), 9 + 12.56),
        (Square(3), Square(2), 9 + 4),
    ],
    ids=["square+triangle", "square+circle", "square+square"]
)
@pytest.mark.smoke
@pytest.mark.square
@pytest.mark.positive
def test_add_area_positive(figure1, figure2, expected_area):
    assert figure1.add_area(figure2) == pytest.approx(expected_area, rel=1e-2), \
        (f"Сумма площадей двух фигур просчитана корректно")


@pytest.mark.parametrize(
    "figure1, figure2",
    [
        (Square(2), 10),
    ],
    ids=["square + not a figure"]
)
@pytest.mark.square
@pytest.mark.negative
def test_add_area_not_figure(figure1, figure2):
    with pytest.raises(ValueError, match="В метод add_area передана не геометрическая фигура"):
        figure1.add_area(figure2)