#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize a square with a private size attribute.
        
        Args:
            size: The size of the square.
        """
        self.__size = size
