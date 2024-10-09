#!/usr/bin/python3
"""
Pascal's Triangle

This module contains a function that generates Pascal's Triangle up to n rows.
Pascal's Triangle is a triangular array of binomial coefficients, where each row
represents the coefficients of the binomial expansion.

Author: Sylvanus Uzor
Date: October 9, 2024
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.
    
    Args:
        n (int): The number of rows in the Pascal's Triangle.
    
    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
        Returns an empty list if n <= 0.
    
    Example:
        pascal_triangle(5) => [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the first row of Pascal's Triangle

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        prev_row = triangle[i - 1]  # Get the previous row

        # Loop to calculate the middle elements of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
