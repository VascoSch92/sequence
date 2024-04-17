from math import gcd, lcm, prod

from sequence.core.core import Sequence


class ArithOp(Sequence):
    """Sequences combined via ArithOpmetic operation, e.g., addition, multiplication.

    Parameters
    ----------
    sequences : List[Sequence]
        List of sequences to combine.
    operation : None, str, function, or numpy ufunc, optional, default = "+""
        if str, must be one of "+" (add), "*" (multiply), "max", "min", "gcd", "lcm"
        if func, must be of signature (1D iterable) -> float
        operation carried out on the sequences
    """

    def __init__(self, sequences, operation="+"):
        super().__init__()
        self.sequences = sequences
        self.operation = operation
        self._op = self._resolve_operation(operation)

    def __add__(self, other):
        if not isinstance(other, ArithOp) or self._op != other._op:
            return ArithOp(sequences=[*self.sequences, other], operation="+")
        else:
            return ArithOp(sequences=[*self.sequences, *other.sequences], operation="+")

    def __mul__(self, other):
        from sequence.sequences.compose.ArithOp import ArithOp

        if not isinstance(other, ArithOp) or self._op != other._op:
            return ArithOp(sequences=[*self.sequences, other], operation="*")
        else:
            return ArithOp(sequences=[*self.sequences, *other.sequences], operation="*")

    def __len__(self):
        lens = [len(sequence) for sequence in self.sequences]
        return min(lens)

    def _resolve_operation(self, operation):
        """Coerce operation to a numpy.ufunc."""
        alias_dict = {
            None: sum,
            "+": sum,
            "add": sum,
            "*": prod,
            "mult": prod,
            "multiply": prod,
            "min": min,
            "max": max,
            "gcd": gcd,
            "lcm": lcm,
        }

        if operation in alias_dict.keys():
            return alias_dict[operation]
        else:
            return operation

    def is_finite(self) -> bool:
        return any(sequence.is_finite() for sequence in self.sequences)

    def _as_generator(self):
        op = self._op
        while True:
            yield op([next(sequence) for sequence in self.sequences])

    def _as_list(self, stop, start=None, step=None):
        op = self._op
        lists = [sequence._as_list(stop, start, step) for sequence in self.sequences]
        return [op(z) for z in zip(*lists)]

    def _at(self, index: int) -> int:
        op = self._op
        ats = [sequence._at(index) for sequence in self.sequences]
        return op(ats)
