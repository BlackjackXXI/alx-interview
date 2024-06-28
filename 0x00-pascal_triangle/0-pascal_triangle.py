#!/usr/bin/python3
"""
a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n

"""

def pascal_triangle(n):
    """
    a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for a in range(1, n + 1):
            level = []
            x = 1
            for j in range(1, a + 1):
                level.append(C)
                x = x * (a - b) // b
            res.append(level)
    return res