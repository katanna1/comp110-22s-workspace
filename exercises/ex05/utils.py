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


# def sub(a_list: list[int], start_index: int, end_index: int) -> str:
#     sub_list: str = ""
#     if start_index < 0:
#         sub_list = sub_list + "a_list[0]"
#     if end_index > len(a_list):
#         last_index: int = len(a_list) - 1
#     if len(a_list) == 0 or start_index > len(a_list) or end_index <= 0:
#         return sub_list