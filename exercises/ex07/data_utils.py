"""Dictionary related utility functions."""

__author__ = "730479768"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table"""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV file line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we are done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = dict()

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a column-oriented table, with only the first n rows of data for each."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        i: int = 0
        while i < rows:
            values.append(table[column][i])
            i = i + 1
        result[column] = values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a column-oriented table with a specefic subset of the original columns"""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = table[column]
    return result


def concat(table: dict[str, list[str]], table1: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-oriented table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table:
        result[column] = table[column]
    for column in table1:
        if column in result:
            i: int = 0
            while i < len(table1[column]):
                result[column].append(table1[column][i])
                i = i + 1
        else:
            result[column] = table1[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key in unique in a list, and is associated with the number of times it appeared in the list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] = result[item] + 1
        else:
            result[item] = 1
    return result