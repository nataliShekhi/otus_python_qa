import pytest
from square import Square


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
    "side_a, area", [(4, 15), (3.5, 15.25)], ids=["integer", "float"]
)
@pytest.mark.smoke
@pytest.mark.square
@pytest.mark.negative
def test_square_area_negative(side_a, area):
    s = Square(side_a)
    assert s.area != area, f"Площадь рассчитан неверно"


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
    "side_a, perimeter", [(4, 14), (3.5, 12)], ids=["integer", "float"]
)
@pytest.mark.square
@pytest.mark.negative
def test_square_perimeter_negative(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter != perimeter, f"Периметр рассчитан неверно"
