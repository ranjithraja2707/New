print("Hello, World"  # Missing closing parenthesis
num = 5 / 0  # Division by zero error
def add_numbers(a, b):
    result = a - b  # Incorrect operation, should be a + b
    return result

print(add_numbers(3, 2))  # Output will be 1 instead of 5
def example_function():
    # Some code here
    if some_condition_not_met:
        raise RuntimeError("This is a runtime error message.")

try:
    example_function()
except RuntimeError as error:
    print(f"Caught an exception: {error}")
def example_function():
print("This is an IndentationError")

