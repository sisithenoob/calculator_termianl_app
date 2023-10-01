#import the Calculation Class from CalculationClass
#it gonna make the code easier to read
#i wanted to work on a two file project to make them work together a first for me  
from CalculationClass import Calculation

#set a variable as an instance of our Calculation Class 
calculator = Calculation()
#variable that check if we want to continue
is_on = True

#loop that makes it possible to make multiple operation one after another without being obligated to rerun the program each time
while is_on == True:
    #give a list of input to the user to choose an operation
    print("""here is list of the calculation your can perform 
          add = +, sus = - , multiply = *, 
          divide = / , exponent = **, square root = sqrt, 
          sin = sin, cos = cos, tan = tan, log = log""")
    choice_operation = input ("enter your operation choice here : ")#user can input its operation choice

    #if statement that check what operation the user chose 
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
        print("the program is not sure what to do. Are you sure you entered a valid input ?") #let know the user that its input whant not valid

    do_continue = input("Do you want to make another operation ? yes or no : ")
    print(do_continue)

    if do_continue == "yes" or do_continue == "Yes":
        is_on == True
    else:
        is_on == False
    print(is_on)
    
    
