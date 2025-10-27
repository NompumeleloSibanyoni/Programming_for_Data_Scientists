def calculator():
    try:
        num1 = float(input())
        num2 = float(input())
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        operator = '+'
    elif choice == '2':
        result = num1 - num2
        operator = '-'
    elif choice == '3':
        result = num1 * num2
        operator = '*'
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operator = '/'
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return

    print(f"\nThe result of {num1} {operator} {num2} is: {result}")

calculator()
