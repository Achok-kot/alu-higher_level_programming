#!/usr/bin/python3
"""Module that provides a function to append text to files."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file in UTF-8 encoding.
    
    Args:
        filename (str): The name of the file to append to. Defaults to empty string.
        text (str): The text content to append to the file. Defaults to empty string.
        
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
