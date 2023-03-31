def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+,-,*,/): ")
    return num1, num2, op
#taking input function

def displayResult(num1, num2, op):
    if op == '+':
        result = num1 + num2
        formula = f"{num1} + {num2} = {result}"
    elif op == '-':
        result = num1 - num2
        formula = f"{num1} - {num2} = {result}"
    elif op == '*':
        result = num1 * num2
        formula = f"{num1} * {num2} = {result}"
    elif op == '/':
        result = num1 / num2
        formula = f"{num1} / {num2} = {result}"
    else:
        print("Invalid operator entered!")
        return
    #decision statement
    print("Formula:", formula)

num1, num2, op = takeInput()
displayResult(num1, num2, op)
