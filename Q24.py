#Program that acts as calculator.Takes two numbers and an operator(+,-,*,/) as inputs and give result

# To add two numbers
def add(num1, num2):
    return num1 + num2
 
# To subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
 
# To multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
# To divide two numbers
def divide(num1, num2):
    return num1 / num2
 
print("""Please select operation 
        1. Add
        2. Subtract
        3. Multiply
        4. Divide""")

operation = int(input("operation operations form 1, 2, 3, 4 :"))
num1 = int(input("Enter first number: "))
num2= int(input("Enter second number: "))
if operation == 1:
    print(num1, "+", num2, "=", add(num1, num2))
 
elif operation == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
 
elif operation == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
 
elif operation == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")






