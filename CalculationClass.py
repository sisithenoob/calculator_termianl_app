import math 

class Calculation():
    

    def sum(self):
        num1 = float(input("What is the first number of your addition : "))
        num2 = float(input("What is the second number of your addition : "))
        print(num1 + num2)
    
    def sus(self):
        num1 = float(input("What is the first number of your sustraction : "))
        num2 = float(("What is the second number of your sustraction : "))
        print(num1 - num2)
    
    def multiply(self):
        num1 = float(input("What is the first number of your multiplication : "))
        num2 = float(input("What is the second number of your multiplication : "))
        print(num1 * num2)
    
    def divide(self):
        num1 = float(input("What is the first number of your division : "))
        num2 = float(input("What is the second number of your division : "))
        print(num1 / num2)

    def exponent(self):
        num1 = float(input(" what is the base of your exponent : "))
        num2 = float(input("what is the the exponential : "))
        print(num1 ** num2)
    
    def square_root(self):
        num = float(input("What is the number that you want the square root of : "))
        print(math.sqrt(num))

    def sinus(self):
        num = float(input("What is the number that you want to perfect the sin function on : "))
        print(math.sin(num))
    
    def cosinus(self):
        num = float(input("What is the number that you want to perfect the cosin function on : "))
        print(math.cos(num))

    def tangent(self):
        num = float(input("What is the number that you want to perfect the tan function on : "))
        print(math.tan(num))

    def log(self):
        base = float(input("Enter your log base : "))
        argument = float(input("enter your log argument here : "))
        print(math.log(argument, base))
    
        
