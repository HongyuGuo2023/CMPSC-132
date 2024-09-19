"""
Name: Hongyu Guo
Course: CMPSC 132
File: Pet_Tester.py
Date: September 17, 2024
Short description: Program for test MyPets modules
"""

from Pet import Pet

# Program description output
def description():
    print('This program is to test the Pet class from Pet module\n')

# Function for pet data display
def petInfo_display(lst):
    print(f'{'Name':<12}{'Type':<12}Age')
    for p in lst:
        print(f'{p.get_name():<12}{p.get_animal_type():<12}{p.get_age()}')

# Main program
def main():
    description()

    # Pet data initialization
    carrot = Pet('Carrot', 'Bird', 2)
    doudou = Pet('Doudou', 'Dog', 6)
    crayon = Pet('Crayon', 'Turtle', 10)

    # Store names in list for the for loop
    pet_list = [carrot, doudou, crayon]

    petInfo_display(pet_list)

if __name__ == '__main__':
    main()

# Sample output
"""
This program is to test the class from MyPet module

Name        Type        Age
Carrot      Bird        2
Doudou      Dog         6
Crayon      Turtle      10
"""
