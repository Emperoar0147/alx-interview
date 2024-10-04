#!/usr/bin/python3

def pascal_triangle(n):
    """
    Pascal's triangle implementation
    Args:
        n: number of rows in the Pascal's triangle
    Return:
        A list of lists representing Pascal's triangle
    """
    triangle = []

    for i in range(n):
        row = [1]  # Start every row with 1
        
        # Calculate the inner values if the row has more than 1 element
        if i > 0:
            for j in range(1, i):
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        
        # End every row with 1 if it's not the first row
        if i > 0:
            row.append(1)
        
        triangle.append(row)  # Append the current row to the triangle

    return triangle
