import pytest
from triangle import Triangle
@pytest.mark.parametrize("side_a,side_b,side_c,area",
    [
        (3, 4, 5, 6),
        (3.5, 4.5, 5.5, 7.854885024620029)
    ],
    ids=['integer', 'float']
)

@pytest.mark.smoke
@pytest.mark.triangle
def test_triangle_area_positive(side_a, side_b, side_c, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.area == area, f'Площадь должна быть {area}'


@pytest.mark.parametrize("side_a,side_b,side_c,area",
    [
        (3, 4, 5, 5),
        (3.5, 4.5, 5.5, 5.854885024620029)
    ],
    ids=['integer', 'float']
)

@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_area_negative(side_a, side_b, side_c, area):
    r = Triangle(side_a, side_b, side_c)
    assert r.area != area, f'Площадь рассчитана некорректно'


@pytest.mark.parametrize("side_a,side_b,side_c,perimeter",
    [
        (3, 4, 5, 12),
        (3.5, 4.5, 5.5, 13.5)
    ],
    ids=['integer', 'float']
)
@pytest.mark.smoke
@pytest.mark.triangle
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.perimeter == perimeter, f'Периметр должен быть равен {perimeter}'


@pytest.mark.parametrize("side_a,side_b,side_c,perimeter",
    [
        (3, 4, 5, 11),
        (3.5, 4.5, 5.5, 13)
    ],
    ids=['integer', 'float']
)
@pytest.mark.negative
@pytest.mark.triangle
def test_triangle_perimeter_negative(side_a, side_b, side_c, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.perimeter != perimeter, f'Периметр рассчитан некорректно'