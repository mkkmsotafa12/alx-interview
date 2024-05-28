#!/usr/bin/python3
"""Pascal Triangle Generator"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Parameters:
    n (int): The number of rows in Pascal's triangle to generate.

    Returns:
    List[List[int]]: A list of lists of integers representing
    Pascal's triangle.
    """

    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle