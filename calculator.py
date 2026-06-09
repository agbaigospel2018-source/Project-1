"""
2. Take an input asking the user what operation to perform
1. Take num1 and num2
3. Check if the selected option exists and carry out the operation
"""

print("_" * 50)
print("Welcome to Timmy's calculators")
print("_" * 50)
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter your second number: "))

print("Select an option below:\nA) Addition\nB) Subtraction\nC) Multiplication\nD) Division")

option = input("==>").upper()

if option == "A":
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
elif option == "B":
    print(f"The difference of {num1} and {num2} is {num1 - num2}")
elif option == "C":
    print(f"The product of {num1} and {num2} is {num1 * num2}")
elif option == "D":
    print(f"The quotient of {num1} and {num2} is {num1 / num2:.2f}")
else:
    print(f"Invalid option {option}")