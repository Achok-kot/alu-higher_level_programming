#!/usr/bin/python3
"""Module that provides a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows.
    
    Args:
        n (int): The number of rows in Pascal's triangle.
        
    Returns:
        list: A list of lists containing Pascal's triangle, or empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    
    return triangle
