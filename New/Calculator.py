def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
print("Calculator Game")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while True:
    try:
        choice = int(input("Enter choice (1-4): "))

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result: ", add(num1, num2))
            elif choice == 2:
                print("Result: ", subtract(num1, num2))
            elif choice == 3:
                print("Result: ", multiply(num1, num2))
            elif choice == 4:
                print("Result: ", divide(num1, num2))
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
