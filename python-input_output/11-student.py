#!/usr/bin/python3
"""Module that defines a Student class with serialization and deserialization."""


class Student:
    """A class that defines a student with serialization capabilities."""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first_name, last_name, and age.
        
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.
        
        Args:
            attrs (list): List of attribute names to retrieve. If None, all attributes.
            
        Returns:
            dict: A dictionary containing specified attributes of the Student.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.
        
        Args:
            json (dict): A dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
