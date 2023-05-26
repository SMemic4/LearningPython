####################################################################################################################################################################
# Chapter 4: Functions
####################################################################################################################################################################
# 4.1 Function Calls
####################################################################################################################################################################
# A function is a named sequence of statements that performs a computation
# When defining a function, specify the name and sequence of statements. The function is then later called by its name
# Example of a function call:

type(32)

# THe name of the function is type. The expression in the parentheses is called the argument of the function
# The argument is a value or variable that is passed into the function as input to the function
# Function often takes an "argument" and returns a "result"

####################################################################################################################################################################
# 4.2 Built-in functions
####################################################################################################################################################################
# Python features a number of important built-in functions
# max() and min() give the largest and smallest values in a list

max("Marsey the orange cat") #>>> "y"

min("Marsey the orange cat") #>>> " "

# The len function tells how many items there are in its argument. If the argument to len is a string that returns the number of characters in the string

len("Marsey the orange cat") # 21 characters

####################################################################################################################################################################
# 4.3 Type conversion functions
####################################################################################################################################################################
# There are built-in functions that convert values from one type to another
# The int() function converts any value to an integer (if it can)

int("32") # 32

int("Marsey") # Error

# int() can covert floating-point values to integers, but doesn't round it off. It chops off the fraction part

int(3.99999) # 3

int(-2.3) # -2

# float() converts integers and strings to floating-point numbers

float(32) # 32.0

float("3.14") # 3.14

# str() converts its argument to a string

str(32) # "32"

str(3.14) # "3.14"

####################################################################################################################################################################
# 4.4 Math Functions
####################################################################################################################################################################
# Python has a math module that provides most of the familiar mathematical functions

import math

# The statement above creates a module object named math. Printing the object provides infomation about it

print(math) # <module 'math' (built-in)>

# THe module object contains the functions and variables defined in the module. 
# To acces one of the function, the name of module must be specified followed by the name of the function seperated by a dot (.). This format is called dot ntation


decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians) # 0.644217687237691

# The first example computes the logarithm base 10 of the singal to noise ratio
# The math module provides a function called log that computes logarithms base e
# THe second example finds the sine of radians. 

# To convert from degrees to radians, divide by 360 and multiply by 2pi

degrees = 45
radians = degrees / 3.60.0 * 2 * math.pi
math.sin(radians) # 0.7853981633974483

# The expression math.pi gets the variable pi from the math modue. The value of this variable is an approximation of pi, accurate to about 15 digits

math.sqrt(2) / 2.0

####################################################################################################################################################################
# 4.5 Random Numbers
####################################################################################################################################################################
# Given the same inputs, most computer programs generate the same outputs everyime. These are called deterministic
# Creating truly  nondeterministic is rather difficult but one way to create them is to use algorithms that generate pseudorandom numbers
# The random module provides functions that generate pseudorandom numbers
# The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0). Each time random is called the next number is chosen in a long series

import random

for i in range(10):
    print(random.randint(0, 10)) # This code generates 10 random numbers between 0 and 10
    
for i in range(10):
    print(random.random()) # This code generate 10 random numbers between 0.0 and 1.0 (but not including 1.0)

# The random function is only one of many functions that handle random numbers. The function randint takes the parameters low and high and returns an interger between log and high (including both)

random.randint(5, 10)

# To chose an element from a sequence at random, use choice()

t = [1,2,3,4,5]
random.choice(t)

# The random module also provides functions to generate random values from continuous distributions including Gaussian, expoential, gamma, and a many more

####################################################################################################################################################################
# 4.6 Adding New Functions
####################################################################################################################################################################
# New functions can be added to Python
# A function definition specifies the name of a new function and the sequence of statements that execute when the function is called. Once a function is defined it be used multiple time throughout the program

def print_lyrics():
  print("Marsey is an orange cat")
  print("Marsey sleeps at least 20 hours a day")

# def is a keyword that indicates that something is a function definition
# The name of the function is print_lyrics
# Empty parenthese after the name indicate that this function doesn't take any arguments
# The first line of the function definition is called the header, the rest is called the body. The header ends with a colon and the body must be indented
# Defining a function creates a variable with the same name
# The value of print_lyrics is a function object, which has type "function"
# Once a function is defined, it can be used inside another function

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

####################################################################################################################################################################
# 4.7 Definitions and Uses
####################################################################################################################################################################
# The program above contains two function definitions: print_lyrics and repeat_lyrics
# Function definitions get executed just like other statements, but the effect is to create function objects. The statements inside the function do not get executed until the function is called and the function definition generates no output
# Functions must be created before they can be executed

####################################################################################################################################################################
# 4.8 Flow of execution
####################################################################################################################################################################
# To ensure that a function is defined before its first use, it most be known which order of the statements are executed. This is termed the flow of execution
# Execution always begins at the first statement of the program. Statements are executed one at a time in order from top to bottom
# Function definitions do not alter the flow of execution of the program, but statements inside the function are not executed until the function is called
# A function call is a like a detour in the flow of execution. Instead of going to the next statement, the flow jumps to the body of the function, executes all the statements there, and then comes back to pick up where it left off

####################################################################################################################################################################
# 4.9 Parameters and Arguments
####################################################################################################################################################################
# Some functions require arguments. For example, when calling math.sin() a number must be passed as an argument. Some arguments take more than one. Math.pow() takes two, the base and the exponent
# Inside functions, arguments are assigned to variables called parameters. An example:

def print_twice(name):
  print(name)
  print(name)
  

print_twice("Marsey")

# The function assigns the argument to a parameter named "name", When the function is called it prints the value of the parameter twice. The function works with any value that can be printed
# The same rules of composition that apply to built-in functions also apply to user-defined functions

print_twice("Marsey "*6)

# The argument is evaulated before the function
# Variables can also be used as an argument

marsey = "Marsey the cat"
print_twice(marsey)

####################################################################################################################################################################
# 4.10 Fruitful functions and void functions
####################################################################################################################################################################
# Some functions such as math functions yield results, these are termed fruitful functions
# Other functions like print_twice() perform an action but don't return a value. These are called void functions
# When caling a fruitful function, ut's important to do something with the result such as assining it to a variable or using it as part of an expression

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

# Whencalling a fruitful function and the result is not stored in a variable the return value disappears

math.sqrt(5) # This script computes the square root of 5, but due to it not storing the result in a variable or displaying the result it is not useful

# Void function might display something on the screen or have some other effect but they don't have a return value. Trying to assign the result to a variable produces a special value called None

result = print_twice("Marsey")
print(result)

# The value None is not the same as the string "None". It is a special value that has its own type

print(type(None)) # <class 'NoneType'>

# To return a result from a function, use a return statement in the function


def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

# When this script executes, the print statement will print ou "8" because the addtwo function was called with 3 and 5 as arguments.
# Within the function, the parameters a and b were 3 and 5 respectively. The function computed the sum of the two numbres and placed it in the local function variable named added
# THen it used the return statement to send the computed value back to the calling code as the function result, which was assigned to the varaible x and printed out

####################################################################################################################################################################
# 4.11 Why functions?
####################################################################################################################################################################
# THere are several reasons to divide a program as a function:
# Creating a new function provides an opportunity to name a group of statements, which makes the program easier to read, understand, and debug
# Functions can make a program smaller by eliminating repetitive code, and changes only need to be made in one place
# Dividing a long program into function all for the code to be debugged at one part at a time
# Well-designed functions are often useful for many programs


####################################################################################################################################################################
# 4.14 Exercises
####################################################################################################################################################################
# 1. What is the purpose of the "def" keyword in python?

# It indicates that the following indented section of code is to be stored for later and that the indented section of code is to be stored for later

# 2. What will the following Python program print out?

def carp():
  print("Zap")
def capy():
  print("ABC"

capy()
carp()
capy()

# It will print out ABC Zap ABC

# 3. Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        x = 40 * rate + ((hours - 40) * (rate * 1.5))
        return x
    else:
        x = hours * rate
        return x


x = computepay(45,10)
print(x)

# 4. Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade():
    x = input("Enter score: ")
    x = int(x)
    try:
        if x >= 90:
            score = "A"
            return score
        elif x >= 80:
            score = "B"
        elif x >= 70:
            score = "C"
        elif x >= 60:
            score = "D"
        else:
            score = "F"

        return score
    except:
        score = "Bad score"
        return score


x = computegrade()
print(x)





 



