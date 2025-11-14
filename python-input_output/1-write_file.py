#!/usr/bin/python3
"""Module that provides a function to write text to files."""


def write_file(filename="", text=""):
    """Write a string to a text file in UTF-8 encoding and return character count.
    
    Args:
        filename (str): The name of the file to write to. Defaults to empty string.
        text (str): The text content to write to the file. Defaults to empty string.
        
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
