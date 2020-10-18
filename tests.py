from pytest import mark

from symmetry import *


# p. 191
segments = [
    (0, 1, 0),
    (1, 0, 1),
    (0, 1, 0, 1, 0),
    (1, 0, 1, 0, 1),
    (1, 1, 1),
    (1, 1),
    (1, 1),
    (1, 0, 1),
    (0, 1, 1, 1, 0),
]


@mark.parametrize(["segment"], [[segment] for segment in segments])
def test_is_symmetrical(segment):
    assert is_symmetrical(segment) == True
