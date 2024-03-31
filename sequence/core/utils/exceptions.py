class PositiveIntegerError(Exception):
    """Error raised when given a negative integer, but a positive integer was expected."""

    def __init__(self, integer: int) -> None:
        super().__init__(f"Expected a positive integer, but got {integer}!")
        self.integer = integer


class StrictlyPositiveIntegerError(Exception):
    """Error raised when given a negative integer, but a strictly positive integer was expected."""

    def __init__(self, integer: int) -> None:
        super().__init__(f"Expected a strictly positive integer, but got {integer}!")
        self.integer = integer


class InfiniteSequenceError(Exception):
    """Error raised when asking for finite sequence property to an infinite sequence."""

    def __init__(self, sequence_name: str) -> None:
        super().__init__(f"The length function is not implemented for {sequence_name}, as the sequence is infinite!")
        self.sequence_name = sequence_name


class NotPeriodicSequenceError(Exception):
    """Error raised when asking period to a non-periodic sequence."""

    def __init__(self, sequence_name: str) -> None:
        super().__init__(f"The {sequence_name} is not periodic!")
        self.sequence_name = sequence_name
