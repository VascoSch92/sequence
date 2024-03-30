from sequence.core.utils.functions import digit_sum
import pytest


@pytest.mark.parametrize(
    "number, base, expected_output",
    [
        (123, 10, 6),
        (0, 10, 0),
        (123, 2, 6),
        (123, 4, 9),
    ],
)
def test_digit_sum(number, base, expected_output):
    if digit_sum(number=number, base=base) != expected_output:
        raise ValueError(f"Expected: {expected_output}, got: {digit_sum(number=number, base=base)}")
