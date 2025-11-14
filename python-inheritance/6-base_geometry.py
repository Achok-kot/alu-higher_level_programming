#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area method."""


class BaseGeometry:
    """A base geometry class."""
    
    def area(self):
        """Calculate the area of the geometry.
        
        Raises:
            Exception: Always raises with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
