# ============================================
# COS202 MATHEMATICAL CALCULATOR
# Name: ________________________
# Matric No: ___________________
# ============================================

def calculator():
    print("=" * 45)
    print("     WELCOME TO MATHEMATICAL CALCULATOR")
    print("=" * 45)

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Floor Division (//)")
        print("6. Modulus (%)")
        print("7. Power (^)")
        print("8. Clear (C)")
        print("9. OFF (Exit)")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "9":
            print("\nCalculator is OFF.")
            print("Thank you for using the Mathematical Calculator.")
            break

        elif choice == "8":
            print("\nScreen Cleared!")
            continue

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                    print(f"\nResult: {num1} + {num2} = {result}")

                elif choice == "2":
                    result = num1 - num2
                    print(f"\nResult: {num1} - {num2} = {result}")

                elif choice == "3":
                    result = num1 * num2
                    print(f"\nResult: {num1} * {num2} = {result}")

                elif choice == "4":
                    if num2 == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        result = num1 / num2
                        print(f"\nResult: {num1} / {num2} = {result}")

                elif choice == "5":
                    if num2 == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        result = num1 // num2
                        print(f"\nResult: {num1} // {num2} = {result}")

                elif choice == "6":
                    if num2 == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        result = num1 % num2
                        print(f"\nResult: {num1} % {num2} = {result}")

                elif choice == "7":
                    result = num1 ** num2
                    print(f"\nResult: {num1} ^ {num2} = {result}")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice! Please select from 1 to 9.")

# Run the calculator
calculator()
