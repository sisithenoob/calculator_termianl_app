from CalculationClass import Calculation
import math

calculator = Calculation()
is_on = True

while is_on == True:
    print("""here is list of the calculation your can perform 
          add = +, sus = - , multiply = *, 
          divide = / , exponent = **, square root = sqrt, 
          sin = sin, cos = cos, tan = tan, log = log""")
    choice_operation = input ("enter your operation choice here : ")

    if choice_operation == "+":
        calculator.sum()
    elif choice_operation == "-":
        calculator.sus()
    elif choice_operation == "*":
        calculator.multiply()
    elif choice_operation == "/":
        calculator.divide()
    elif choice_operation == "**":
        calculator.exponent()
    elif choice_operation == "sqrt":
        calculator.square_root()
    elif choice_operation == "sin":
        calculator.sinus()
    elif choice_operation == "cos":
        calculator.cosinus()
    elif choice_operation == "tan":
        calculator.tangent()
    elif choice_operation == "log":
        calculator.log()
    else:
        print("the program is not sure what to do. Are you sure you entered a valid input ?")

    do_continue = input("Do you want to make another operation ? yes or no : ")
    print(do_continue)

    if do_continue == "yes" or do_continue == "Yes":
        is_on == True
    else:
        is_on == False
    print(is_on)
    
    
