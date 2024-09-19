"""
Name: Hongyu Guo
Course: CMPSC 132
File: Grade_Tester.py
Date: September 4, 2024
Short description: Program for test Grade.py module
"""

from Grade import calc_average, grade_converter

# Program description output
def description():
    print('This program is to test the function from Grade module\n')

# Function ask for grades
def ask_grade():
    # First loop ensure grade is integer
    while True:
        try:
            grades = int(input('How many grades you would like to enter: '))
            if grades <= 0: # Ensure integer is not 0 to avoid 0 division error
                print('<!> Please enter positive integer.')
            else:
                break

        except ValueError:
            print('<!> Invalid input, please enter valid integer.')
    # Create empty list to store grades
    grade_list = []
    # For loop to repeat based on grade numbers
    for g in range(grades):
        # Loop to ensure each input are in range 0 - 100
        while True:
            try:
                grade = float(input(f'Please enter the grade {g+1}: '))
                if (grade < 0) or (grade > 100):
                    print('<!> please enter valid number.')
                else: # If valid, append grade into list
                    grade_list.append(grade)
                    break

            except ValueError:
                print('<!> Invalid input, please enter valid number.')
    # Output grade list
    return grade_list
# Main program
def main():

    description()

    while True:

        # Getting grades from user and calculate for average
        lst = ask_grade()
        average = calc_average(lst)

        # Average result display
        print(f'\nThe average of the total score is {average:.2f}.')
        letter_grade = grade_converter(average)
        # Letter score display
        print(f'The letter score of the average is {letter_grade}')

        # Ask user if they want to start a new round
        user_answer = input('\nDo you want to test more grades? (yes/no): ').strip().lower()
        # Ensure valid input
        while (user_answer != 'yes') and (user_answer != 'no'):
            user_answer = input('<!> Please enter a valid answer.'
                                '\nDo you want to test more grades? (yes/no): ').strip().lower()
        # Allow user to start a new round
        if user_answer == 'yes':
            print('Starting new round...\n')
            continue
        # End the program
        else:
            print('Grade testing completed.')
            break

if __name__ == '__main__':
    main()

# Testing result sample output
"""
<Normal run>
This program is to test the function from Grade module

How many grades you would like to enter: 5
Please enter the grade 1: 80
Please enter the grade 2: 95
Please enter the grade 3: 88
Please enter the grade 4: 74
Please enter the grade 5: 83

The average of the total score is 84.00.
The letter score of the average is B

Do you want to test more grades? (yes/no): no
Grade testing completed.

<Error testing>
This program is to test the function from Grade module

How many grades you would like to enter: -5
<!> Please enter positive integer.
How many grades you would like to enter: !@#
<!> Invalid input, please enter valid integer.
How many grades you would like to enter: 5
Please enter the grade 1: -88
<!> please enter valid number.
Please enter the grade 1: 88
Please enter the grade 2: !@#
<!> Invalid input, please enter valid number.
Please enter the grade 2: 77
Please enter the grade 3: <>?>
<!> Invalid input, please enter valid number.
Please enter the grade 3: 66
Please enter the grade 4: -124
<!> please enter valid number.
Please enter the grade 4: 55
Please enter the grade 5: 12!@#
<!> Invalid input, please enter valid number.
Please enter the grade 5: 44

The average of the total score is 66.00.
The letter score of the average is D

Do you want to test more grades? (yes/no): -2
<!> Please enter a valid answer.
Do you want to test more grades? (yes/no): !@#
<!> Please enter a valid answer.
Do you want to test more grades? (yes/no): yes
Starting new round...

How many grades you would like to enter: 5
Please enter the grade 1: 20
Please enter the grade 2: 40
Please enter the grade 3: 60
Please enter the grade 4: 80
Please enter the grade 5: 100

The average of the total score is 60.00.
The letter score of the average is D

Do you want to test more grades? (yes/no): no
Grade testing completed.
"""