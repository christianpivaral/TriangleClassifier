from triangle import classify_triangle


def test_customer_manufacturing_requirements():
    # Wall panel: three equal sides
    assert classify_triangle(24, 24, 24) == "Equilateral"

    # Flooring tile: right-angle triangular tile
    assert classify_triangle(9, 12, 15) == "Right Scalene"

    # Custom mirror: impossible dimensions
    assert classify_triangle(10, 15, 30) == "Invalid"