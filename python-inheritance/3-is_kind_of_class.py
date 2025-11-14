#!/usr/bin/python3
"""Module that provides a function to check class instance or inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of or inherits from the specified class.
    
    Args:
        obj: The object to check
        a_class: The class to compare against
        
    Returns:
        bool: True if obj is instance of a_class or inherits from it
    """
    return isinstance(obj, a_class)
