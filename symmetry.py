from math import ceil, floor
from typing import Sequence, Literal

__all__ = ["is_symmetrical"]

Bit = Literal[0, 1]

def is_symmetrical(segment: Sequence[Bit]) -> int:
    n = len(segment)

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
