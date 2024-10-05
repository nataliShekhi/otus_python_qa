import math
import pytest
from circle import Circle


@pytest.mark.parametrize(
    "radius,area",
    [(3, round(math.pi * 3 ** 2, 2)), (3.5, round(math.pi * 3.5 ** 2, 2))],
    ids=["integer", "float"],
    )
def test_circle_area_positive(radius, area):
    r = Circle(radius)
    assert r.area == pytest.approx(area, rel=1e-2), f"Площадь должна быть {area}"


@pytest.mark.parametrize(
    "radius,perimeter",
    [(3, round(2 * math.pi * 3)), (3.5, round(2 * math.pi * 3.5))],
    ids=["integer", "float"],
)
@pytest.mark.smoke
@pytest.mark.circle
def test_circle_perimeter_positive(radius, perimeter):
    r = Circle(radius)
    assert r.perimeter == pytest.approx(perimeter, rel=1e-2), f"Периметр должен быть равен {perimeter}"


@pytest.mark.parametrize(
    "radius", [(-3)], ids=["negative radius"]
)
@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.circle
def test_circle_incorrect_values(radius):
    r = Circle(radius)
    assert r.radius <= 0, f"Радиус круга не может быть равен или меньше 0"


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        (Circle(4), Circle(2), 50.26 + 12.56),
    ],
    ids=["circle+circle"]
)
@pytest.mark.smoke
@pytest.mark.circle
@pytest.mark.positive
def test_add_area_positive(figure1, figure2, expected_area):
    assert figure1.add_area(figure2) == pytest.approx(expected_area, rel=1e-2), \
        (f"Сумма площадей двух фигур просчитана корректно")


@pytest.mark.parametrize(
    "figure1, figure2",
    [
        (Circle(4), 10),
    ],
    ids=["circle + not a figure"]
)
@pytest.mark.circle
@pytest.mark.negative
def test_add_area_not_figure(figure1, figure2):
    with pytest.raises(ValueError, match="В метод add_area передана не геометрическая фигура"):
        figure1.add_area(figure2)