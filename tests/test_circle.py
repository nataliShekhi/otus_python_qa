import pytest
from circle import Circle


@pytest.mark.parametrize(
    "radius,area",
    [(3, 28.274333882308138), (3.5, 38.48451000647496)],
    ids=["integer", "float"],
)
@pytest.mark.smoke
@pytest.mark.circle
def test_circle_area_positive(radius, area):
    r = Circle(radius)
    assert r.area == area, f"Площадь должна быть {area}"


@pytest.mark.parametrize(
    "radius,area", [(3, 28.27), (3.5, 39.48451000647496)], ids=["integer", "float"]
)
@pytest.mark.negative
@pytest.mark.circle
def test_circle_area_negative(radius, area):
    r = Circle(radius)
    assert r.area != area, f"Площадь рассчитана некорректно"


@pytest.mark.parametrize(
    "radius,perimeter",
    [(3, 18.84955592153876), (3.5, 21.991148575128552)],
    ids=["integer", "float"],
)
@pytest.mark.smoke
@pytest.mark.circle
def test_circle_perimeter_positive(radius, perimeter):
    r = Circle(radius)
    assert r.perimeter == perimeter, f"Периметр должен быть равен {perimeter}"


@pytest.mark.parametrize(
    "radius,perimeter", [(3, 19.8495), (3.5, 23.9911485)], ids=["integer", "float"]
)
@pytest.mark.negative
@pytest.mark.circle
def test_circle_perimeter_negative(radius, perimeter):
    r = Circle(radius)
    assert r.perimeter != perimeter, f"Периметр рассчитан некорректно"


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
        (Circle(4), Circle(2), 50.2654824 + 12.566370614359172),
    ],
    ids=["circle+circle"]
)
@pytest.mark.smoke
@pytest.mark.circle
@pytest.mark.positive
def test_add_area_positive(figure1, figure2, expected_area):
    assert figure1.add_area(figure2) == pytest.approx(expected_area), \
        (f"Сумма площадей двух фигур просчитана корректно")


@pytest.mark.parametrize(
    "figure1, figure2, expected_area",
    [
        (Circle(4), Circle(2), 50.2654 + 12.5663),
    ],
    ids=["circle+circle"]
)
@pytest.mark.circle
@pytest.mark.negative
def test_add_area_negative(figure1, figure2, expected_area):
    assert figure1.add_area(figure2) != pytest.approx(expected_area), \
        (f"Сумма площадей двух фигур просчитана некорректно")


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