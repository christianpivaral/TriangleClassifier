
import math


def is_valid_triangle(a, b, c) -> bool:
    # Check for zero, negative, or non-finite side lengths
    if not all(math.isfinite(side) and side > 0 for side in (a, b, c)):
        return False

    # The sum of any two sides must be greater than the third
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True


def classify_triangle(a, b, c) -> str:
    # Check if the sides form a valid triangle
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    # Determine the triangle type based on equal sides
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Sort the sides so the largest is last
    sides = sorted([a, b, c])

    # Scale the sides to avoid overflow with large numbers
    largest = sides[2]
    x = sides[0] / largest
    y = sides[1] / largest

    # Check the Pythagorean theorem using relative tolerance
    if math.isclose(
        x ** 2 + y ** 2,
        1.0,
        rel_tol=1e-9,
        abs_tol=0.0
    ):
        return "Right " + triangle_type

    return triangle_type


# Manual tests
if __name__ == "__main__":
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(5, 5, 5))
    print(classify_triangle(5, 5, 8))
    print(classify_triangle(3, 4, 6))
    print(classify_triangle(1, 2, 3))

    # Test the floating-point issue Copilot identified
    print(classify_triangle(3e-6, 4e-6, 5.0001e-6))
