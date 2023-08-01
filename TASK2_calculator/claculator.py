def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_user_input()

def get_operation_choice():
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter the operation number (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError
        return choice
    except ValueError:
        print("Invalid input. Please enter a valid operation number.")
        return get_operation_choice()

def perform_calculation(num1, num2, choice):
    if choice == 1:
        return add(num1, num2)
    elif choice == 2:
        return subtract(num1, num2)
    elif choice == 3:
        return multiply(num1, num2)
    elif choice == 4:
        return divide(num1, num2)

def main():
    try:
        num1, num2 = get_user_input()
        choice = get_operation_choice()

        result = perform_calculation(num1, num2, choice)

        print("Result: ", result)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
