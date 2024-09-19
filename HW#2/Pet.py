"""
Name: Hongyu Guo
Course: CMPSC 132
File: Pet.py
Date: September 17, 2024
Short description: A class to represent pets, including attributes for pet information,
                   and get and set methods.
"""

# Define pet class
class Pet:
    def __init__(self, name = None, animal_type = None, age = 0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Set method for pet
    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_type):
        self.__animal_type = new_type

    def set_age(self, new_age):
        self.__age = new_age

    # Get method for pet
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

if __name__ == '__main__':
    p0 = Pet()
    p0.set_name('Arnold')
    p0.set_animal_type('Doggy')
    p0.set_age(4)
    print(p0.get_name(), p0.get_animal_type(), p0.get_age())
