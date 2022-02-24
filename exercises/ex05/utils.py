"""Implementing function skeletons."""

__author__ = "730479768"


def only_evens(a_list: list[int]) -> list[int]:
    """Returns even integers in a list format."""
    i: int = 0
    evens_list: list[int] = []
    while i < len(evens_list):
        if evens_list[i] % 2 == 0:
            evens_list.append(evens_list[i])
        i = i + 1
    return (evens_list)


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Creates a seperate set of integers from the orignal."""
    subset: list[int] = []
    if len(a_list) == 0:
        return subset
    if start_index >= len(a_list):
        return subset
    if end_index <= 0:
        return subset
    if start_index < 0:
        subset.append(a_list[0])
    else:
        subset.append(a_list[start_index])
    if end_index > len(a_list):
        subset.append(a_list[len(a_list) - 1])
    else:
        subset.append(a_list[end_index - 1])
    return subset


def concat(a: list[int], b: list[int]) -> list[int]:
    """This function creates a new list with integers from both lists."""
    together: list[int] = []
    together = a
    i: int = 0
    while i < len(b):
        num_b: int = b[i]
        together.append(num_b)
        i = i + 1
    return together