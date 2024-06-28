#!/usr/bin/python3
'''a function def pascal_triangle(n): that returns a list of lists of integers 
'''


def pascal_triangle(n):
    '''a function def pascal_triangle(n): that returns a list of lists of integers 
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle