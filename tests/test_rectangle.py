import pytest
from rectangle import Rectangle

@pytest.mark.parametrize("side_a,side_b,area",
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ],
    ids=['integer', 'float']
)

@pytest.mark.smoke
@pytest.mark.rectangle
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Площадь для чисел {side_a} и {side_b} должна быть {area}'

@pytest.mark.parametrize("side_a,side_b,area",
    [
        (3, 5, 14),
        (3.5, 5.5, 17.25)
    ],
    ids=['integer', 'float']
)

@pytest.mark.negative
@pytest.mark.rectangle
def test_rectangle_area_negative(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area != area, f'Площадь для чисел {side_a} и {side_b} не равна {area}'

@pytest.mark.parametrize("side_a,side_b,perimeter",
    [
        (3, 5, 16),
        (3.5, 5.5, 18)
    ],
    ids=['integer', 'float']
)
@pytest.mark.smoke
@pytest.mark.rectangle
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, f'Периметр для чисел {side_a} и {side_b} должен быть равен {perimeter}'

@pytest.mark.parametrize("side_a,side_b,perimeter",
    [
        (3, 5, 15),
        (3.5, 5.5, 12)
    ],
    ids=['integer', 'float']
)
@pytest.mark.negative
@pytest.mark.rectangle
def test_rectangle_perimeter_negative(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter != perimeter, f'Периметр для чисел {side_a} и {side_b} не равен {perimeter}'
