# Program to create a calculator

import os 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

operations_dict = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calculator():
    number1 = float(input("Enter the first number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
        op_symbol = input("Enter an operation: ")
        number2 = float(input("Enter the second number: "))
        calculator_function = operations_dict[op_symbol]
        output = calculator_function(number1, number2)
        print(f'{number1} {symbol} {number2} = {output}')

        should_continue = input(f"Enter 'y' to continue operation with {output} or 'n' to start a new operation or 'x' to exit operation ").lower()
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag = False
            print("Bye")
            
calculator()