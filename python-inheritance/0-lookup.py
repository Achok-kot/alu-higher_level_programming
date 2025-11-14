#!/usr/bin/python3
"""Module that provides a lookup function to get object attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object to inspect
        
    Returns:
        list: A list of strings containing all attributes and methods of the object
    """
    return dir(obj)
