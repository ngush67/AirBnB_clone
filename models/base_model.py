#!/usr/bin/env python3
'''the basemodel module'''
import datetime
import uuid
from models import storage


class BaseModel:
    '''defines all common attributes/methods to be inherited'''

    def __init__(self, *args, **kwargs):
        # if kwargs is not empty, re-create instance from a dictionary
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    "datetime; from string to date"
                    value = datetime.datetime.fromisoformat(value)
                    self.__setattr__(key, value)
                else:
                    self.__setattr__(key, value)
        else:
            '''initializes public instance attributes'''
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        '''prints [class name] (id) dict'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the updated_at attribute with current datetime'''
        self.updated_at = datetime.datetime.now()
        storage.save(self.to_dict())

    def to_dict(self):
        '''return a dict with all keys/values of this instance's __dict__'''
        instance_dict = self.__dict__

        # add a class, convert updated/created_at to strings
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['updated_at'] = str(instance_dict['updated_at'])
        instance_dict['created_at'] = str(instance_dict['created_at'])
        return instance_dict


"""
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
"""

