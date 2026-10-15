# Triangle Classifier — CSC 325

## Project Overview

This project is a Python triangle classifier that checks whether three side lengths form a valid triangle. If they do, the program identifies the triangle as equilateral, isosceles, or scalene. It also checks whether the triangle has a right angle.

The project uses pytest for unit and acceptance testing. GitHub Copilot was used to suggest unit tests, which were reviewed before being accepted.

## How to Run the Tests

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

Run all tests:

```bash
python -m pytest -v
```

Run only the unit tests:

```bash
python -m pytest -v test_triangle.py
```

Run the acceptance test:

```bash
python -m pytest -v test_acceptance.py
```

## Equivalence Classes

The tests cover several different types of triangle inputs:

- **Invalid sides:** A side is zero or negative.
- **Degenerate triangles:** Two sides add up to exactly the third side.
- **Equilateral:** All three sides are equal.
- **Isosceles:** Exactly two sides are equal.
- **Scalene:** All three sides are different.
- **Right triangles:** The side lengths satisfy the Pythagorean theorem within a tolerance.

## Boundary Testing

I tested zero and negative side lengths because triangles cannot have those measurements.

I also tested degenerate triangles, where two sides add up to the third side. These should be invalid because they do not form a proper triangle.

Another issue involved floating-point precision. A very small triangle with sides `(3e-6, 4e-6, 5.0001e-6)` was incorrectly classified as a right triangle. After reproducing the problem, the tolerance calculation was corrected and a regression test was added.

## Acceptance Criteria

The acceptance test uses three manufacturing examples: triangular wall panels, flooring tiles, and custom mirrors.

**1. Decorative Wall Panels**

A customer orders a wall panel with three sides measuring 24 inches. The program should return `Equilateral` because all three sides are equal.

**2. Triangular Flooring Tiles**

A customer orders a flooring tile with sides measuring 9, 12, and 15 inches. The program should return `Right Scalene` because the measurements form a right triangle with three different sides.

**3. Custom Triangle Mirrors**

A customer submits mirror measurements of 10, 15, and 30 inches. Since the measurements cannot form a triangle, the program should return `Invalid` without crashing.

## Copilot Review Log

| Test or review | Copilot suggested? | Decision | Reason |
|---|---|---|---|
| Invalid side tests | Yes | Kept | Checked zero and negative sides in different positions. |
| Degenerate triangle tests | Yes | Kept | Verified that sides adding up to the third side return `Invalid`. |
| Equilateral, isosceles, and scalene tests | Yes | Kept | The expected classifications matched the assignment. |
| Integer right-triangle test | Yes | Kept | Correctly expected `Right Scalene` for sides 3, 4, and 5. |
| Non-integer right-triangle test | Yes | Kept | Correctly expected `Right Isosceles` for sides 5, 5, and 5 × √2. |
| Floating-point edge-case review | Yes | Investigated and corrected | Copilot identified an incorrect classification caused by the original absolute tolerance. I reproduced the issue, changed the implementation, and added a regression test. |

Copilot's original unit tests passed, but the additional review identified a problem they did not cover. This demonstrated why passing tests alone does not guarantee that every edge case has been handled.

## Test Results

The final test run completed with **16 passing tests**, including 15 unit test cases and one acceptance test.

## Right Equilateral Triangles

An equilateral triangle cannot also be a right triangle in Euclidean geometry. All three interior angles of an equilateral triangle are 60 degrees, so none can be 90 degrees.

## AI Use Disclosure

GitHub Copilot was used to generate initial unit-test suggestions and review the code for additional edge cases. The suggestions were checked against the assignment requirements, and the tests were run using pytest.

ChatGPT was also used to assist with the implementation, debugging, test development, and documentation. The floating-point classification issue was investigated and corrected after Copilot identified it.

The acceptance test covers manufacturing examples involving wall panels, flooring tiles, and mirrors. AI assistance was also used in developing these examples and assertions.

All 16 test cases passed during the final pytest run.
