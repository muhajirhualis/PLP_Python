# Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

def calculator():

  num1 = float(input("Write 1st Number:"))
  num2 = float(input("Write 2nd Number:"))
  operation = input("Choose the operation: ").strip()

  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    if num2 != 0:
      result = num1 / num2
    else:
      result = ("❌ Error: Division by zero is not allowed!")
  else: 
    print("Incorrect Operation! Please choose +, -, *, or /")
  
  print(f"Result: {result}")

calculator()