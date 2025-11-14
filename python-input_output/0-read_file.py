#!/usr/bin/python3
"""Module that provides a function to read and print text files."""


def read_file(filename=""):
    """Read a text file in UTF-8 encoding and print its contents to stdout.
    
    Args:
        filename (str): The name of the file to read. Defaults to empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
