#!/usr/bin/python3
"""
This modules defines class FileStorage that serializes instances
to a JSON file and deserializes a JSON file to instances
"""
import json
import os


class FileStorage:
    """
    Serializes and deserializes instances
    """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects attribute

        Args:
            obj (object): An object with key <obj class name>.id
        """
        key = f"{obj['__class__']}.{obj['id']}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value
        with open(FileStorage.__file_path, 'a', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects

        Returns:
            (obj): returns __objects from a JSON file
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
