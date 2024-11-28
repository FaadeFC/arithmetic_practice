import os
from random import randint


def get_range():
    """ Return the minimum and maximum for the range. """
    minimum = int(input("Minimum: "))
    maximum = int(input("Maximum: "))
    return (minimum, maximum)


def clear():
    os.system("cls")


def main():
    """ Execute the main program. """
    operation = " "

    while True:
        clear()
        operation = input("(1) Addition\n(2) Subtraction\n(3) Multiplication \n(4) Division\n\n")
        clear()

        if operation != "1" and operation != "2" and operation != "3" and operation != "4":
            break

        try:
            (minimum, maximum) = get_range()
        except:
            break

        clear()
        guess = 0

        while True:
            # Get both of the numbers.
            a = randint(minimum, maximum)
            b = randint(minimum, maximum)
            answer = 0
            operation_string = ""

            # Get the operation and the answer.
            if operation == "1":
                operation_string = "+"
                answer = str(a + b)
            if operation == "2":
                operation_string = "-"
                answer = str(a - b)
            if operation == "3":
                operation_string = "*"
                answer = str(a * b)
            if operation == "4":
                operation_string = "/"
                if a % b == 0:
                    answer = str(a // b)
                else:
                    answer = str(a // b) + "r" + str(a % b)
            
            print(f"{a} {operation_string} {b}\n")
            guess = input("Guess: ")
            
            if guess == "":
                break
            elif guess == answer:
                print("Correct")
            else:
                print(f"Incorrect: {answer}")
            
            input()
            clear()


main()