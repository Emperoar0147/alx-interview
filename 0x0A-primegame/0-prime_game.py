#!/usr/bin/python3
"""
module that house a function
"""

def island_perimeter(grid):
    """
    function to calculate and return the perimeter of an island
    Args:
      grid: 2D array that represent the island
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Start with 4 edges
                perimeter += 4

                # Check for neighboring land cells to subtract shared edges
                if r > 0 and grid[r-1][c] == 1:  # Top neighbor
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:  # Bottom neighbor
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:  # Left neighbor
                    perimeter -= 1
                if c < cols - 1 and grid[r][c+1] == 1:  # Right neighbor
                    perimeter -= 1

    return perimeter
