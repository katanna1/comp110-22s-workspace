"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, max, linkify, scale, value_at

__author__ = "730479768"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_max_empty() -> None:
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    linked = Node(1, Node(2, Node(3, None)))
    assert max(linked) == 3


def test_linkify_empty() -> None:
    x: list[int] = []
    assert linkify(x) is None


def test_linkify_non_empty() -> None:
    list = [1, 2, 3]
    assert str(linkify(list)) == "1 -> 2 -> 3 -> None"


def test_scale_empty() -> None:
    assert scale(None, 4) is None


def test_scale_non_empty() -> None:
    linked = Node(1, Node(2, Node(3, None)))
    assert str(scale(linked, 3)) == "3 -> 6 -> 9 -> None"


def test_value_at_empty() -> None:
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_non_empty() -> None:
    linked = Node(1, Node(2, Node(3, None)))
    assert value_at(linked, 1) == 2