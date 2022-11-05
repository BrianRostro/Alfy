def calc_math_expression(num1, num2, operator):
    num1 = float(input("Please enter first number: "))
    num2 = float(input("Please enter second number: "))
    operator = input("Please enter an operator: ")
    
    if operator == "+":
        print(num1 + num2)

calc_math_expression()