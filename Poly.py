class Calculator:
    def add(self, num1, num2=0):
        return num1 + num2


# Example usage
calc = Calculator()

# Call add method with one parameter
result1 = calc.add(5)
print("Result with one parameter:", result1)  # Output: Result with one parameter: 5

# Call add method with two parameters
result2 = calc.add(3, 7)
print("Result with two parameters:", result2)  # Output: Result with two parameters: 10

