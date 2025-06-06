import pytest
from hypothesis import given, strategies as st
import math

def circle_area(radius):
    """Вычисляет площадь круга с защитой от малых значений"""
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    if radius < 1e-100:  # Игнорируем слишком малые значения
        return 0.0
    return math.pi * radius ** 2

@given(st.floats(min_value=0, max_value=1e6, allow_nan=False, allow_infinity=False))
def test_circle_area_non_negative(radius):
    """Площадь круга всегда неотрицательна"""
    area = circle_area(radius)
    assert area >= 0

@given(
    st.floats(min_value=1e-10, max_value=1e5),  # Избегаем слишком малых значений
    st.floats(min_value=1e-10, max_value=1e5)
)
def test_circle_area_monotonic(r1, r2):
    """Площадь монотонно возрастает с ростом радиуса"""
    if r1 < r2:
        assert circle_area(r1) < circle_area(r2)
    elif r1 > r2:
        assert circle_area(r1) > circle_area(r2)
    else:
        assert circle_area(r1) == circle_area(r2)

@given(st.floats(min_value=1, max_value=1))
def test_circle_area_value(radius):
    """Проверка конкретного значения"""
    assert abs(circle_area(radius) - math.pi < 1e-10)

@given(st.floats(max_value=-1e-6, allow_nan=False, allow_infinity=False))
def test_circle_area_negative_radius(radius):
    """Отрицательный радиус вызывает исключение"""
    with pytest.raises(ValueError):
        circle_area(radius)

if __name__ == "__main__":
    pytest.main(["-v", "--hypothesis-show-statistics"])