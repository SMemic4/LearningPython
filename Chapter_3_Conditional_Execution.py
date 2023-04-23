library(reticulate)
####################################################################################################################################################################
# Chapter 3: Conditional Execution
####################################################################################################################################################################
# 3.1 Boolean Expressions

# A boolean expression is an expression that is either true or false
# The following expression uses the operator ==, which compares two operands and produces True if they are equal and False otherwise:

5 == 5 # True

5 == 6 # False

# True and False are special values that belong to the class bool; they are not strings

type(True) # <class 'bool'>

type(False) # <class 'bool'>

# The == operator is one of the comparison operators the others are:

x != y # x is not equal to y
x > y # x is greater than y 
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y
x is y # x is the same as y
x is not y # x is not the same as y

# A common mistake to avoid is using a single equal sign (=) instead of the double equal sign (==)
# The = is an assignment operator and == is a comparison operator
# There is not such thing as =< or => (Equal sign always follows the angle bracket)

####################################################################################################################################################################
# 3.2 LOgical OPerators

# There are three logical operators: and, or, and not 

x > 0 and x < 10

# The expression above is only true if x is greater than - and less than 10

n%2 == 0 or n%3 == 0

# The expression above is only true if either of the conditions is true, that is, if the number is divisble by 2 or 3

# The not operator negates a boolean expression

not (x > y)

# The expression above is true if x ? y is false, that is if x is less than or equal to u

# Any nonzero number is interpreted as "true""

17 and True # True

####################################################################################################################################################################
# 3.3 Conditional execution

# In order to write useful programs, it is important to have the ability to check conditions and change the behavior of the program accordingly
# Conditional statements grant this ability. The simplest form is the if statement:

x = 10
if (x > 0): 
     print("x is positive")

# The boolean expression after the if statement is called the condition. The if statement ends with a colon character (:) and the lines after the if statement are indented
# If the logical condition is true, then the indented statement gets executed. If the logical condition is fals ethe indented statement is skipped

# if statements have the same structure as funtion definitions or for loops
# Statements like this are called compound statements because they strech across more than one line
# THere is no limit on the number of statements that can appear in the body, but there must be at least one
# To write an if statement with no statements or a place holder, a pass statement can be put into the loop

if (x > 0):
   pass

if (x > 10):
    print("Small")
  


# When entering an if statement, the prompt will change from three > to three dots to indicate the code is in the middle of a block of statements

####################################################################################################################################################################
# 3.4 Alternative execution



