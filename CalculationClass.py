#import the math module make the code way easier to read and it is easier to implement the sqrt, trig function, and log logic with it
import math 

#this is the class that contain all of the operation our calculator will inherit, and will be able to do/
class Calculation():
    
    #addition function
    def sum(self):
        num1 = float(input("What is the first number of your addition : "))#take first num of add
        num2 = float(input("What is the second number of your addition : "))#take second num of add
        print(num1 + num2)#print result of the operation
    
    #sustraction function work exactly the same as sum
    def sus(self):
        num1 = float(input("What is the first number of your sustraction : "))
        num2 = float(("What is the second number of your sustraction : "))
        print(num1 - num2)
    
    #mulplication function work the same as sum
    def multiply(self):
        num1 = float(input("What is the first number of your multiplication : "))
        num2 = float(input("What is the second number of your multiplication : "))
        print(num1 * num2)
    
    #division function work the same as sum
    def divide(self):
        num1 = float(input("What is the first number of your division : "))
        num2 = float(input("What is the second number of your division : "))
        print(num1 / num2)

    #exponential function
    def exponent(self):
        num1 = float(input(" what is the base of your exponent : "))#take the base of the exponent
        num2 = float(input("what is the the exponential : "))#take the exponent of the base
        print(num1 ** num2)#print the result 
    
    #square root function 
    def square_root(self):
        num = float(input("What is the number that you want the square root of : "))#take one num to return its sqrt
        print(math.sqrt(num))#print result

    #sin function work exactly the same as square root
    def sinus(self):
        num = float(input("What is the number that you want to perfect the sin function on : "))
        print(math.sin(num))
    
    #cos function work exactly the same as square root
    def cosinus(self):
        num = float(input("What is the number that you want to perfect the cosin function on : "))
        print(math.cos(num))

    #tan function work exactly the same as square root
    def tangent(self):
        num = float(input("What is the number that you want to perfect the tan function on : "))
        print(math.tan(num))

    #logarithm function
    def log(self):
        base = float(input("Enter your log base : "))#take the base of our log
        argument = float(input("enter your log argument here : "))#take the argument of the log
        print(math.log(argument, base))#print the result
    
        
