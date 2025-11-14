#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list."""


class MyList(list):
    """A list subclass with additional functionality to print sorted content."""
    
    def print_sorted(self):
        """Print the list in sorted order without modifying the original list."""
        print(sorted(self))

