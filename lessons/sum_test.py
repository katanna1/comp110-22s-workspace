"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0