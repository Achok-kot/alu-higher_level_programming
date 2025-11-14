#!/usr/bin/python3
"""Module that defines a BaseGeometry class with validation."""


class BaseGeometry:
    """A base geometry class with area and validation methods."""
    
    def area(self):
        """Calculate the area of the geometry.
        
        Raises:
            Exception: Always raises with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate that value is a positive integer.
        
        Args:
            name (str): The name of the parameter
            value: The value to validate
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
