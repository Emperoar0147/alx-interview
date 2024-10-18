#!/usr/bin/python3
"""
Module 0-minoperations
This module defines the `minOperations` function, which calculates the
minimum number of operations required to achieve exactly n characters
using only "Copy All" and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The number of H characters to achieve.

    Returns:
        int: The minimum number of operations or 0 if it's not possible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
