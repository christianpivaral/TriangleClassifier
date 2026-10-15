import math
import pytest
from triangle import classify_triangle


@pytest.mark.parametrize(
	("sides",),
	[
		((0, 4, 5),),
		((4, 0, 5),),
		((4, 5, 0),),
		((-1, 4, 5),),
		((4, -1, 5),),
		((4, 5, -1),),
	],
)
def test_zero_or_negative_side_is_invalid(sides):
	assert classify_triangle(*sides) == "Invalid"


@pytest.mark.parametrize(
	("sides",),
	[
		((1, 2, 3),),
		((1, 3, 2),),
		((3, 1, 2),),
	],
)
def test_degenerate_triangle_is_invalid(sides):
	assert classify_triangle(*sides) == "Invalid"


def test_equilateral_triangle():
	assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles_triangle():
	assert classify_triangle(5, 5, 8) == "Isosceles"


def test_scalene_triangle():
	assert classify_triangle(3, 4, 6) == "Scalene"


def test_integer_right_triangle():
	assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_non_integer_right_triangle():
	assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"

def test_small_non_right_triangle():
    # Regression test for the floating-point tolerance bug
    # These sides form a scalene triangle, not a right triangle
    assert classify_triangle(3e-6, 4e-6, 5.0001e-6) == "Scalene"    