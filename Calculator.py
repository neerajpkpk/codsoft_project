def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user
    operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")

    # Validate the operation choice
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation choice. Please try again.")
        return

    try:
        # Input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the chosen operation
    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        # Handle division by zero
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

# Run the calculator
calculator()
