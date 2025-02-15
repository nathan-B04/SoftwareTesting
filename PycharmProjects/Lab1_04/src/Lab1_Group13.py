import random
import string

# Title: Random Secure Password Generator
# Author: Nathan Bricknell, Syed Ali Sajjad Naqvi
# Date: February 13 2025
""" 
Purpose: To generate a protected password
depending on the input the user gives.
"""

#Variables
restart = 1
password_array = []
password_length = 0
user_input = 0

# --Integer validation--
def valid_input(question, min_value=0):
    while True:
        try:
            user_input = int(input(question))
            if user_input >= min_value:
                return user_input
            else:
                print(f"Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# --Welcome Message--
print("Welcome to the Password Generator")


# While loop that will reset the program
while restart == 1:
    # User input must be above 7 to proceed to the next loop
    while user_input <= 7:
        user_input = valid_input("What is the total length for your password (8 or above): ")
        if user_input >= 8:
            password_length = int(user_input)  # Assign user input's value to password_length
            # Error messages for anything not an int greater than 7
        if user_input < 7:
            print("Your password is too short.")

    # --Numbers--
    while True:
        user_input = valid_input("\nHow many characters are numbers?: ")
        # User input needs to be less than or equal to the password length to proceed
        if user_input <= password_length:
            # Add user input to the password_array using the random.choices generator for the numbers
            password_array.extend(random.choices(string.digits, k=user_input))
            # Subtract the value of numbers used within the password length
            password_length -= user_input
            break
        else:
            print("More characters than password length.") # Errors

    # --Letters--
    # Same notes at above
    while True:
        user_input = valid_input("How many characters are letters?: ")
        if user_input <= password_length:
            password_array.extend(random.choices(string.ascii_letters, k=user_input))
            password_length -= user_input
            break
        else:
            print("More characters than password length.\n")

    # --Special Characters--
    # Same notes as above
    while True:
        user_input = valid_input("How many characters are special characters?: ")
        if user_input <= password_length:
            password_array.extend(random.choices(string.punctuation, k=user_input))
            password_length -= user_input
            break
        else:
            print("More characters than password length.\n")

    # Ensures the password is above 0
    if password_length > 0:
        # Adding all the stores values together
        password_array.extend(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

    # random.shuffle to mix the characters up so they are not in order of numbers, letter, and special characters
    random.shuffle(password_array)

    print("\nYour password is: ", "".join(password_array))
    reset_input = input("Would you like to restart the program? (y/n): ")
    if reset_input == "y":
        restart = 1 # To restart the program
    else:
        restart = 0 # To switch the loop off