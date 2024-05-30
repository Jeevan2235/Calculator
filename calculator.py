def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = int(input("Please select the first number."))
    for sign in operations:
        print(sign)
    should_continue = True

    while should_continue:
        operation = input("Please select the operation.")
        num2 = int(input("Please select the second number."))

        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'Y' to continue calculating with the {answer}, or type 'n' to start a new calculation.") == 'Y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

