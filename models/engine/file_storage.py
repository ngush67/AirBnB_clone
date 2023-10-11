#!/usr/bin/env python3
"""Store objects to json"""
import json


class FileStorage:
    '''
    serializes py instances to JSON and 
    deserializes JSON strings to py instances
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects
        
    def new(self, obj):
        '''sets [obj_class_name.id]:obj in __objects'''
        record_key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[record_key] = obj

    def save(self):
        '''serializes __objects to the JSON file given as class attr'''
        with open(self.__file_path, 'w') as my_file:
            json.dump(self.__objects, my_file)

    def reload(self):
        '''deserializes the json file to __objects iff the json file exists'''
        try:
            with open(self.__file_path, 'r') as my_file:
                self.__objects = json.load(my_file)
        except FileNotFoundError:
            pass

