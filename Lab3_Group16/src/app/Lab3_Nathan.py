from math import pi

def valid_input(question):
    while True:
        try:
            user_input = float(input(question))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def valid_char(char_question, min_char, max_char):
    while True:
        user_char = input(char_question).lower()
        if user_char in [min_char, max_char]:
            return user_char
        else:
            print(f"Please enter a valid character (y/n).")

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return round(pi * (r ** 2), 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

def trapezium_area(a, b, h):
    #Using all() like a list with a variable in x
    if all(isinstance(x, (int, float)) and x >= 0 for x in (a, b, h)):
        #rounding to nearest tenth
        return round(0.5 * (a + b) * h, 2)
    #Value error
    raise ValueError("a, b, and h must be non-negative numbers.")

def ellipse_area(a, b):
    if all(isinstance(x, (int, float)) and x >= 0 for x in (a,b)):
        return round(pi * a * b, 2)
    raise ValueError("Invalid radius. Must be a non-negative number.")

def rhombus_area(p, q):
    if all(isinstance(x, (int, float)) and x >= 0 for x in (p,q)):
        return round(0.5 * (p * q), 2)
    raise ValueError("Invalid radius. Must be a non-negative number.")

"""restart = "y"

while restart == "y":
    print("\n1. Circle\n2. Trapezoid\n3. Ellipse\n4. Rhombus\n5. Quit")
    user_input = input("\nPlease enter your choice: ")
    if user_input == "1":
        print("\nCircle")
        circle_input = valid_input("Enter radius: ")
        radius = circle_input
        circle = circle_area(radius)
        print (f"The circle's area is {circle}".format(circle=circle))
        user_choice = valid_char("return to menu? y/n: ", 'y', 'n')
        if user_choice == 'n':
            restart = 'n'

    elif user_input == "2":
        trap_input = valid_input("Enter first base: ")
        base_one = trap_input
        trap_input = valid_input("Enter second base: ")
        base_two = trap_input
        trap_input = valid_input("Enter height: ")
        height = trap_input
        trap = trapezium_area(base_one, base_two, height)
        print (f"The trapezoid area is {trap}".format(trap=trap))
        user_choice = valid_char("return to menu? y/n: ", 'y', 'n')
        if user_choice == 'n':
            restart = 'n'

    elif user_input == "3":
        ellipse_input = valid_input("Enter first axis: ")
        axis_one = ellipse_input
        ellipse_input = valid_input("Enter second axis: ")
        axis_two = ellipse_input
        ellipse = ellipse_area(axis_one, axis_two)
        print (f"The ellipse area is {ellipse}" .format(ellipse=ellipse))
        user_choice = valid_char("return to menu? y/n: ", 'y', 'n')
        if user_choice == 'n':
            restart = 'n'

    elif user_input == "4":
        rhombus_input = valid_input("Enter p diagonal: ")
        p_diagonal = rhombus_input
        rhombus_input = valid_input("Enter q diagonal: ")
        q_diagonal = rhombus_input
        rhombus = rhombus_area(p_diagonal, q_diagonal)
        print (f"The rhombus area is {rhombus}" .format(rhombus=rhombus))
        user_choice = valid_char("return to menu? y/n: ", 'y', 'n')
        if user_choice == 'n':
            restart = 'n'

    elif user_input == "5":
        print("Closing Program...")
        restart = "n"

    else:
        print("Invalid input. Please enter a number 1 to 5.")"""