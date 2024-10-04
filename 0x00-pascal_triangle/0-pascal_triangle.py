#!/usr/bin/python3


def pascal_triangle(n):
    """
    pascal triangle implementation
    args:
         n: number of rows in the pascal triangle
    return:
         a list of pascal triangle based on the rows given
    """
    triangle = []

    for i in range(n):
        row = [1]  # Start the row with 1's

        # Calculate the inner elements (skipping the first and last)
        if i > 1:
            for j in range(1, i):
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)

        if i > 0:
            row.append(1)

        triangle.append(row)  # Append the current row to the triangle

    return triangle
