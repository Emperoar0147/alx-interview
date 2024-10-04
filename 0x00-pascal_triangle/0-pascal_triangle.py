def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle up to row n."""
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the remaining rows
    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Compute the new value as the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
