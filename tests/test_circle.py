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
