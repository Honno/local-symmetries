from math import ceil, floor
from typing import Literal, Sequence, Iterator, Tuple

from more_itertools import substrings

__all__ = ["is_symmetrical", "count_symmetries"]


Bit = Literal[0, 1]


def is_symmetrical(segment: Sequence[Bit]) -> int:
    n = len(segment)

    if n == 0 or n == 1:
        return False

    if n % 2 == 0:
        mid = n // 2
        head, tail = segment[:mid], segment[mid:]
    else:
        mid = n / 2
        lower, upper = floor(mid), ceil(mid)
        head, tail = segment[:lower], segment[upper:]

    for left, right in zip(head, reversed(tail)):
        if left != right:
            return False
    else:
        return True


def count_symmetries(sequence: Sequence[Bit]) -> int:
    nsymmetries = 0
    for segment in substrings(sequence):
        if is_symmetrical(segment):
            nsymmetries += 1

    return nsymmetries
