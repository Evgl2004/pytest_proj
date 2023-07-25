import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


@pytest.mark.parametrize('array, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([43, 211, 1, 0], -2, 3, [1]),
    ([9, 10, 8, 11], -6, -2, [9, 10]),
    ([], None, None, [])

])
def test_slice(array, start, end, expected):
    assert arrs.my_slice(array, start, end) == expected


