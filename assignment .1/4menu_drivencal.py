# Task 1
while True:
    # 1. Display menu
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Exit")

# Task 2
    choice = int(input("Enter your choice (1-7): "))

    if choice == 7:
        print("Exiting calculator. Goodbye from calculator by shaurya!")
        break

# Task 3
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

# Task 4
    if choice == 1:
        print(f"Result: {a} + {b} = {a + b}")
    elif choice == 2:
        print(f"Result: {a} - {b} = {a - b}")
    elif choice == 3:
        print(f"Result: {a} * {b} = {a * b}")
    elif choice == 4:
        if b != 0:   # 9. Division-by-zero handling
            print(f"Result: {a} / {b} = {a / b}")
        else:
            print("Error: Division by zero is not allowed!")
    elif choice == 5:
        print(f"Result: {a} % {b} = {a % b}")
    elif choice == 6:
        print(f"Result: {a} ** {b} = {a ** b}")
    else:
# Task 5
        print("Invalid choice! Please select from 1 to 7.")
