#!/usr/bin/python3
""" Module for calculating minimum operations """


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): The number of H characters to achieve

    Returns:
        int: The minimum number of operations
    """
    if n <= 1:
        return 0

    op = 0
    fac = 2

    while n > 1:
        while n % fac == 0:
            op += fac
            n //= fac
        fac += 1

    return op
