import pytest

from sequence.core.utils.exceptions import (
    PositiveIntegerError,
    StrictlyPositiveIntegerError,
)
from sequence.core.utils.validation import (
    validate_integer,
    validate_as_list_input,
    validate_positive_integer,
    validate_strictly_positive_integer,
    validate_given_length_integer_tuple,
)


@pytest.mark.parametrize("integer", [-123, -23, 0, 1, 2134, 2398493284])
def test_validate_integer(integer) -> None:
    if integer != validate_integer(integer=integer):
        raise ValueError(f"Expected: {integer}. Got {validate_integer(integer=integer)}")


@pytest.mark.parametrize("integer", [23.23, "asd", [], {"asd": 23.23}, {123}])
def test_error_validate_integer(integer) -> None:
    with pytest.raises(ValueError):
        _ = validate_integer(integer=integer)


@pytest.mark.parametrize("integer", [0, 1, 1, 2, 3, 5, 8, 123])
def test_validate_positive_integer(integer) -> None:
    if integer != validate_positive_integer(integer=integer):
        raise ValueError(f"Expected: {integer}. Got {validate_integer(integer=integer)}")


@pytest.mark.parametrize(
    "integer, error",
    [
        (23.23, ValueError),
        ("asd", ValueError),
        (-12, PositiveIntegerError),
    ],
)
def test_error_validate_positive_integer(integer, error) -> None:
    with pytest.raises(error):
        _ = validate_positive_integer(integer=integer)


@pytest.mark.parametrize("integer", [1, 10, 2, 3, 5, 8, 123])
def test_validate_strictly_positive_integer(integer) -> None:
    if integer != validate_strictly_positive_integer(integer=integer):
        raise ValueError(f"Expected: {integer}. Got {validate_integer(integer=integer)}")


@pytest.mark.parametrize(
    "integer, error",
    [
        (23.23, ValueError),
        ("asd", ValueError),
        (-12, StrictlyPositiveIntegerError),
        (0, StrictlyPositiveIntegerError),
    ],
)
def test_error_validate_strictly_positive_integer(integer, error) -> None:
    with pytest.raises(error):
        _ = validate_strictly_positive_integer(integer=integer)


@pytest.mark.parametrize("tuple, length", [((1, 2, 3), 3), ((), 0)])
def test_validate_given_length_integer_tuple(tuple, length) -> None:
    validate_given_length_integer_tuple(tuple=tuple, length=length)


@pytest.mark.parametrize("tuple, length", [((1, 2, 3), 2), ([], 0), ((1, 2, 3.1), 3)])
def test_error_validate_given_length_integer_tuple(tuple, length) -> None:
    with pytest.raises(ValueError):
        validate_given_length_integer_tuple(tuple=tuple, length=length)


@pytest.mark.parametrize(
    "input_values, expected_values", [((2, 1, 3), (2, 1, 3)), ((2, None, 3), (2, 0, 3)), ((2, 1, None), (2, 1, 1))]
)
def test_validate_as_list_input(input_values, expected_values) -> None:
    output = validate_as_list_input(
        stop=input_values[0],
        start=input_values[1],
        step=input_values[2],
    )
    if output != expected_values:
        raise ValueError(f"Expected: {expected_values}. Got {output}!")
