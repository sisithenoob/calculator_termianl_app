import math 

class Calculation():
    

    def sum():
        num1 = input("What is the first number of your addition : ")
        num2 = input("What is the second number of your addition : ")
        return num1 + num2
    
    def sus():
        num1 = input("What is the first number of your sustraction : ")
        num2 = input("What is the second number of your sustraction : ")
        return num1 - num2
    
    def multiply():
        num1 = input("What is the first number of your multiplication : ")
        num2 = input("What is the second number of your multiplication : ")
        return num1 * num2
    
    def divide():
        num1 = input("What is the first number of your division : ")
        num2 = input("What is the second number of your division : ")
        return num1 - num2

    def exponent():
        num1 = input(" what is the base of your exponent : ")
        num2 = input("what is the the exponential : ")
        return num1 ** num2
    
    def square_root():
        num = input("What is the number that you want the square root of : ")
        return math.sqrt(num)

    def sinus():
        num = input("What is the number that you want to perfect the sin function on : ")
        return math.sin(num)
    
    def cosinus():
        num = input("What is the number that you want to perfect the cosin function on : ")
        return math.cos(num)

    def tangent():
        num = input("What is the number that you want to perfect the tan function on : ")
        return math.tan(num)

    def log():
        base = input("Enter your log base : ")
        argument = input("enter your log argument here : ")
        return math.log(argument, base)
    
        
