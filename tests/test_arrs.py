from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([43, 211, 1, 0], -2, 3) == [1]
    assert arrs.my_slice([9, 10, 8, 11], -6, -2) == [9, 10]
    assert arrs.my_slice([]) == []
