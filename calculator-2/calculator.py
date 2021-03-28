"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Please type an operator and two numbers: ")
    tokens = user_input.split(" ")

    if tokens[0].lower() == 'q' or tokens[1] == 'q':
        print('You quit...')
        break
    else:
        operator = tokens[0]
        num1 = tokens[1]
        num1 = float(num1)

        if len(tokens) < 3:
            num2 = 0
        else:
            num2 = tokens[2]
            num2 = float(num2)

        result = None

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            result = num1 / num2

        elif operator == "square":
            result = num1 ** 2

        elif operator.lower() == "cube" or operator.lower() == "c":
            result = num1 ** 3

        elif operator.lower == "pow" or operator.lower() == "p":
            result = num1 ** num2

        elif operator.lower() == "mod" or operator.lower() == "m":
            result = num1 % num2

        print(result)