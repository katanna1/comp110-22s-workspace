"""Unit test functions of the dictionary file."""


__author__ = "730479768"


from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


def test_invert_edge() -> None:
    """Tests the invert function with an edge case."""
    with pytest.raises(KeyError):
        a: dict[str, str] = {"Clarke": "Griffin", "Bellamy": "Blake", "Raven": "Reyes", "Octavia": "Blake"}
        invert(a)


def test_invert_use() -> None:
    """Tests invert function for a typical case."""
    a: dict[str, str] = {"a": "b", "c": "d", "e": "f", "g": "h"}
    assert invert(a) == {"b": "a", "d": "c", "f": "e", "h": "g"}
    

def test_invert_use1() -> None:
    """Tests another invert function for a typical case."""
    a: dict[str, str] = {"red": "orange", "yellow": "green", "blue": "violet", "black": "white"}
    assert invert(a) == {"orange": "red", "green": "yellow", "violet": "blue", "white": "black"}


def test_favorite_color_edge() -> None:
    """Tests the favorite color function for an edge case."""
    a: dict[str, str] = {"Katrina": "green", "Wayne": "red", "Inna": "yellow", "Michelle": "green", "Alexandra": "yellow"}
    assert favorite_color(a) == "green"


def test_favorite_color_use() -> None:
    """Tests the favorite color function for a typical use case."""
    a: dict[str, str] = {"Octavia": "red", "Bellamy": "blue", "Murphy": "yellow", "Emori": "green", "Lincoln": "blue"}
    assert favorite_color(a) == "blue"


def test_favorite_color_use1() -> None:
    """Tests the favorite color function another time for a typical use case."""
    a: dict[str, str] = {"Sasha": "pink", "Glenn": "blue", "Maggie": "purple", "Abraham": "green", "Denise": "pink"}
    assert favorite_color(a) == "pink"


def test_count_edge() -> None:
    """Tests the count function with an edge case."""
    a: list[str] = ["a", "b", "c", "d", "e"]
    assert count(a) == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1}


def test_count_use() -> None:
    """Tests the count function with a typical use case."""
    a: list[str] = ["rose", "sunflower", "daisy", "rose", "tulip", "daisy", "fern", "rose"]
    assert count(a) == {"rose": 3, "sunflower": 1, "daisy": 2, "tulip": 1, "fern": 1}


def test_count_use1() -> None:
    """Tests the count function another time with a typical use case."""
    a: list[str] = ["cake", "cookie", "pudding", "cake", "pudding", "icecream"]
    assert count(a) == {"cake": 2, "cookie": 1, "pudding": 2, "icecream": 1}