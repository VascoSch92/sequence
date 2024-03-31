from typing import Any

from sequence.core.mixin import MonotonicIncreasingMixin
from sequence.core.infinite_type import Explicit
from sequence.core.utils.functions import digit_sum
from sequence.sequences.integer.explicit_generalised import (
    DigitSumSequence,
    PolygonalNumbers,
    GeneralisedNexusNumbers,
)


class A000027(Explicit):
    """The natural numbers (https://oeis.org/A000027)."""

    SEQUENCE_NAME = "natural numbers"

    def __contains__(self, item: Any) -> bool:
        return True

    def formula(self, index: int) -> int:
        return index


PositiveIntegers = A000027
NaturalNumbers = A000027


class A000120(DigitSumSequence):
    """Number of 1's in binary expansion of n (https://oeis.org/A000120)."""

    SEQUENCE_NAME = "sequence A000120"

    def __init__(self) -> None:
        super().__init__(base=2)


class A000217(PolygonalNumbers):
    """Triangular numbers (https://oeis.org/A000217)."""

    SEQUENCE_NAME = "triangular numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=3)


TriangularNumbers = A000217


class A000290(Explicit):
    """Square numbers (https://oeis.org/A000290)."""

    SEQUENCE_NAME = "square numbers"

    def __contains__(self, item: Any) -> bool:
        return False if item < 0 else int(item ** (1 / 2)) == item ** (1 / 2)

    def formula(self, index: int) -> int:
        return index**2


SquareNumbers = A000290


class A000326(PolygonalNumbers):
    """Pentagonal numbers (https://oeis.org/A000326)."""

    SEQUENCE_NAME = "pentagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=5)


PentagonalNumbers = A000326


class A000384(PolygonalNumbers):
    """Hexagonal numbers (https://oeis.org/A000384)."""

    SEQUENCE_NAME = "hexagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=6)


HexagonalNumbers = A000384


class A000566(PolygonalNumbers):
    """Heptagonal numbers (https://oeis.org/A000566)"""

    SEQUENCE_NAME = "heptagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=7)


HeptagonalNumbers = A000566


class A000567(PolygonalNumbers):
    """Octagonal numbers (https://oeis.org/A000567)"""

    SEQUENCE_NAME = "octagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=8)


OctagonalNumbers = A000567


class A001045(MonotonicIncreasingMixin, Explicit):
    """Jacobsthal numbers (https://oeis.org/A001045)."""

    SEQUENCE_NAME = "Jacobsthal numbers"

    def formula(self, index: int) -> int:
        return round(2**index / 3)


JacobsthalNumbers = A001045
JacobsthalSequence = A001045


class A001106(PolygonalNumbers):
    """Nonagonal numbers (https://oeis.org/A001106)"""

    SEQUENCE_NAME = "nonagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=9)


NonagonalNumbers = A001106


class A001107(PolygonalNumbers):
    """Decagonal numbers (https://oeis.org/A001107)"""

    SEQUENCE_NAME = "decagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=10)


DecagonalNumbers = A001107


class A003215(GeneralisedNexusNumbers):
    """Hex (or centered hexagonal) numbers (https://oeis.org/A003215)."""

    SEQUENCE_NAME = "hex numbers"

    def __init__(self) -> None:
        super().__init__(dimension=2)

    def __contains__(self, item: Any) -> bool:
        if item <= 0:
            return False
        n = (3 + (12 * item - 3) ** (1 / 2)) / 6
        return n == int(n)


HexNumbers = A003215
CenteredHexagonalNumbers = A003215


class A005408(Explicit):
    """The odd numbers (https://oeis.org/A005408)."""

    SEQUENCE_NAME = "odd numbers"

    def __contains__(self, item: Any) -> bool:
        return item % 2 == 1

    def formula(self, index: int) -> int:
        return 2 * index + 1


OddNumbers = A005408


class A007953(DigitSumSequence):
    """Digital sum (i.e., sum of digits) of n (https://oeis.org/A007953)."""

    SEQUENCE_NAME = "digsum"

    def __init__(self) -> None:
        super().__init__(base=10)


Digsum = A007953


class A010060(Explicit):
    """Thue-Morse sequence (https://oeis.org/A010060)."""

    SEQUENCE_NAME = "Thue-Morse sequence"

    def __contains__(self, item: Any) -> bool:
        return item in [0, 1]

    def formula(self, index: int) -> int:
        return digit_sum(number=index, base=2) % 2


ThueMorseSequence = A010060


class A014551(MonotonicIncreasingMixin, Explicit):
    """Jacobsthal-Lucas numbers (https://oeis.org/A014551)."""

    SEQUENCE_NAME = "Jacobsthal-Lucas numbers"

    def __contains__(self, item: Any) -> bool:
        if item == 1:
            return True
        return super().__contains__(item=item)

    def formula(self, index: int) -> int:
        return 2**index + (-1) ** index


JachobsthalLucasNumbers = A014551


class A033999(Explicit):
    """Sequence of powers of -1 (https://oeis.org/A033999)."""

    SEQUENCE_NAME = "sequence of powers of -1"

    def __contains__(self, item: Any) -> bool:
        return item in {-1, 1}

    def formula(self, index: int) -> int:
        return (-1) ** index


class A051624(PolygonalNumbers):
    """Dodecagonal numbers https://oeis.org/A051624)."""

    SEQUENCE_NAME = "dodecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=12)


DodecagonalNumbers = A051624


class A051682(PolygonalNumbers):
    """Hendecagonal numbers (https://oeis.org/A051682)."""

    SEQUENCE_NAME = "hendecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=11)


HendecagonalNumbers = A051682


class A051865(PolygonalNumbers):
    """Tridecagonal numbers (https://oeis.org/A051865)."""

    SEQUENCE_NAME = "tridecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=13)


TridecagonalNumbers = A051865


class A051866(PolygonalNumbers):
    """Tetradecagonal numbers (https://oeis.org/A051866)."""

    SEQUENCE_NAME = "tetradecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=14)


TetradecagonalNumbers = A051866


class A051867(PolygonalNumbers):
    """Pentadecagonal numbers (https://oeis.org/A051867)."""

    SEQUENCE_NAME = "pentadecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=15)


PentadecagonalNumbers = A051867


class A051868(PolygonalNumbers):
    """Hexadecagonal numbers (https://oeis.org/A051868)."""

    SEQUENCE_NAME = "hexadecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=16)


HexadecagonalNumbers = A051868


class A051869(PolygonalNumbers):
    """Heptadecagonal numbers (https://oeis.org/A051869)."""

    SEQUENCE_NAME = "heptadecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=17)


HeptadecagonalNumbers = A051869


class A051870(PolygonalNumbers):
    """Octadecagonal numbers (https://oeis.org/A051870)."""

    SEQUENCE_NAME = "octadecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=18)


OctadecagonalNumbers = A051870


class A051871(PolygonalNumbers):
    """Enneadecagonal numbers (https://oeis.org/A051871)."""

    SEQUENCE_NAME = "enneadecagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=19)


EnneadecagonalNumbers = A051871


class A051872(PolygonalNumbers):
    """Icosagonal numbers (https://oeis.org/A051872)."""

    SEQUENCE_NAME = "icosagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=20)


IcosagonalNumbers = A051872


class A051873(PolygonalNumbers):
    """Icosihenagonal numbers (https://oeis.org/A051873)."""

    SEQUENCE_NAME = "icosihenagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=21)


IcosihenagonalNumbers = A051873


class A051874(PolygonalNumbers):
    """Icosidigonal numbers (https://oeis.org/A051874)."""

    SEQUENCE_NAME = "icosidigonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=22)


IcosidigonalNumbers = A051874


class A051875(PolygonalNumbers):
    """Icositrigonal numbers (https://oeis.org/A051875)."""

    SEQUENCE_NAME = "icositrigonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=23)


IcositrigonalNumbers = A051875


class A051876(PolygonalNumbers):
    """Icositetragonal numbers (https://oeis.org/A051876)."""

    SEQUENCE_NAME = "icositetragonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=24)


IcositetragonalNumbers = A051876


class A053735(DigitSumSequence):
    """Sum of digits of n written in base 3 (https://oeis.org/A053735)."""

    SEQUENCE_NAME = "sequence A053735"

    def __init__(self) -> None:
        super().__init__(base=3)


class A053737(DigitSumSequence):
    """Sum of digits of n written in base 4 (https://oeis.org/A053737)."""

    SEQUENCE_NAME = "sequence A053737"

    def __init__(self) -> None:
        super().__init__(base=4)


class A053824(DigitSumSequence):
    """Sum of digits of n written in base 5 (https://oeis.org/A053824)."""

    SEQUENCE_NAME = "sequence A053824"

    def __init__(self) -> None:
        super().__init__(base=5)


class A053827(DigitSumSequence):
    """Sum of digits of n written in base 6 (https://oeis.org/A053827)."""

    SEQUENCE_NAME = "sequence A053827"

    def __init__(self) -> None:
        super().__init__(base=6)


class A053828(DigitSumSequence):
    """Sum of digits of n written in base 7 (https://oeis.org/A053828)."""

    SEQUENCE_NAME = "sequence A053828"

    def __init__(self) -> None:
        super().__init__(base=7)


class A053829(DigitSumSequence):
    """Sum of digits of n written in base 8 (https://oeis.org/A053829)."""

    SEQUENCE_NAME = "sequence A053829"

    def __init__(self) -> None:
        super().__init__(base=8)


class A053830(DigitSumSequence):
    """Sum of digits of n written in base 9 (htpps://oeis.org/A053830)."""

    SEQUENCE_NAME = "sequence A053830"

    def __init__(self) -> None:
        super().__init__(base=9)


class A167149(PolygonalNumbers):
    """Myriagonal numbers (https://oeis.org/A167149)."""

    SEQUENCE_NAME = "myriagonal numbers"

    def __init__(self) -> None:
        super().__init__(number_of_sides=10_000)


MyriagonalNumbers = A167149
