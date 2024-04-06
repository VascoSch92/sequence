from sequence.core.core import Sequence

import numpy as np


class Arith(Sequence):
    """Sequences combined via arithmetic operation, e.g., addition, multiplication.

    Parameters
    ----------
    sequences : List[Sequence]
        List of sequences to combine.
    operation : None, str, function, or numpy ufunc, optional, default = None = mean
        if str, must be one of "mean", "+" (add), "*" (multiply), "max", "min"
        if func, must be of signature (1D iterable) -> float
        operation carried out on the sequences
    """

    def __init__(self, sequences, operation):
        super().__init__()
        self.sequences = sequences
        self.operation = operation
        self._op = self._resolve_operation(operation)

    def __add__(self, other):
        if not isinstance(other, Arith) or self._op != other._op:
            return Arith(sequences=[*self.sequences, other], operation="+")
        else:
            return Arith(sequences=[*self.sequences, *other.sequences], operation="+")

    def __mul__(self, other):
        from sequence.sequences.compose.arith import Arith

        if not isinstance(other, Arith) or self._op != other._op:
            return Arith(sequences=[*self.sequences, other], operation="*")
        else:
            return Arith(sequences=[*self.sequences, *other.sequences], operation="*")

    def _resolve_operation(self, operation):
        """Coerce operation to a numpy.ufunc."""
        alias_dict = {
            None: np.mean,
            "mean": np.mean,
            "+": np.add,
            "add": np.add,
            "*": np.multiply,
            "mult": np.multiply,
            "multiply": np.multiply,
            "min": np.min,
            "max": np.max,
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
