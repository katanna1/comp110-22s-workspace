"""Function skeletons and implementations."""


__author__ = "730479768"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Function inverts the keys and values from one dictionary to another."""
    inverted: dict[str, str] = {}
    for key in a:
        if a[key] in inverted:
            raise KeyError("Two keys cannot have the same name.")
        inverted[a[key]] = key
    return inverted


def main() -> None:
    """Main procedure to call the favorite_color function from."""
    print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def favorite_color(a: dict[str, str]) -> str:
    """Finds what color name is found most frequently in a dictionary."""
    color_num: int = 0
    color: str = ""
    color_count: dict[str, int] = {}
    for key in a:
        if a[key] in color_count:
            color_count[a[key]] += 1
        else:
            color_count[a[key]] = 1
    for key in color_count:
        if color_num < color_count[key]:
            color_num = color_count[a[key]]
            color = key
    return color


def count(a: list[str]) -> dict[str, int]:
    """Counts how many times an item appears in a list."""
    i: int = 0
    count1: dict[str, int] = {}
    while len(a) > i:
        if a[i] in count1:
            count1[a[i]] += 1
        else:
            count1[a[i]] = 1
    i = i + 1
    return count1


if __name__ == "__main__":
    main()