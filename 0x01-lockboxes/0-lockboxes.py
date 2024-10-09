#!/usr/bin/python3
"""
Lockboxes Problem

This script provides a solution to the lockboxes problem, where you are given n boxes,
each containing keys to other boxes. The goal is to determine whether all boxes can be unlocked.
The solution uses a depth-first search (DFS) algorithm to traverse through the boxes and keys.

Author: Sylvanus Uzor
Date: October 9, 2024
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    Args:
        boxes (list of lists): A list where each element is a list of keys found in a box.
                               The index of the list represents the box number.
    
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    
    Example:
        boxes = [[1], [2], [3], [4], []]
        canUnlockAll(boxes) => True
    
    This function uses a set to track unlocked boxes and a DFS (using a stack) to traverse
    through the keys and unlock as many boxes as possible.
    """
    
    n = len(boxes)  # Number of boxes
    unlocked_boxes = set([0])  # Start with the first box unlocked
    keys = [0]  # List to store keys (start with the first box's key)
    
    # Iterate while there are keys to process
    while keys:
        box = keys.pop()  # Get the current box to open
        
        # Loop through all the keys found in the current box
        for key in boxes[box]:
            # Only unlock if it's a valid box and not already unlocked
            if key not in unlocked_boxes and key < n:
                unlocked_boxes.add(key)  # Mark the box as unlocked
                keys.append(key)  # Add the key to the stack for further exploration
    
    # Return True if all boxes have been unlocked, else return False
    return len(unlocked_boxes) == n
