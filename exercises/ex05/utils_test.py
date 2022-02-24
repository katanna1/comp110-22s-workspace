"""Tests for the utility list skeleton functions."""

__author__ = "730479768"


from utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    """Tests the edge case for which are even numbers."""
    a: list[int] = [1, 3, 5, 7, 9, 11, 13]
    assert only_evens(a) == []


def test_only_evens_use() -> None:
    """Tests a use case for the only evens function."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(a) == [2, 4, 6]


def test_only_evens_use1() -> None:
    """Second test for another average use case for the only evens function."""
    a: list[int] = [14, 15, 16, 17, 18, 19, 20, 21]
    assert only_evens(a) == [14, 16, 18, 20]


def test_sub_edge() -> None:
    """Tests the edge case for an end value which is greater than the list length in the sub function."""
    a: list[int] = [1, 3, 5, 7, 9, 11, 13]
    assert sub(a, 0, 7) == [1, 13]


def test_sub_use() -> None:
    """Tests the typical use case for the sub function."""
    a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sub(a, 2, 6) == [3, 6]


def test_sub_use1() -> None:
    """Tests another of a typical use case for the sub function."""
    a: list[int] = [31, 32, 33, 34, 35, 36, 37, 38]
    assert sub(a, 1, 4) == [32, 34]


def test_concat_edge() -> None:
    """Tests the edge case incase one of the lists is empty."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    b: list[int] = []
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]


def test_concat_use() -> None:
    """Tests a typical use case for the concat function."""
    a: list[int] = [1, 2, 3, 4]
    b: list[int] = [5, 6, 7, 8]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_use1() -> None:
    """Tests another typical use case for the concat function."""
    a: list[int] = [15, 20, 27, 39]
    b: list[int] = [12, 32, 60, 62]
    assert concat(a, b) == [15, 20, 27, 39, 12, 32, 60, 62]