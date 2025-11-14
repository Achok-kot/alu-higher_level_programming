#!/usr/bin/python3
"""Module that provides a function to save objects to JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.
    
    Args:
        my_obj: The object to save to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
