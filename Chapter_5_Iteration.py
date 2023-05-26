####################################################################################################################################################################
# Chapter 5: Iteration
####################################################################################################################################################################
# 5.1 Updating Variables
####################################################################################################################################################################
# A common pattern in assignment statements is an assignment statement that updates a variable, where the new value of the variable depends on the old

x = x + 1

# Trying to update a variable that doesn't exist, causes an error

x = x + 1 # name "x" is not defined

# Before a variable can be updated, it must be initialized, usually with a simple assignment

x = 0
x = x +1

# Updating a variable by adding 1 is called an incremenet; subtracting 1 is called a decrement 

####################################################################################################################################################################
# 5.2 The while statement
####################################################################################################################################################################
#  Phython provides several language features to make iteration easier
# One form of iteration in Pythn is the while statement. 

n = 5
while n > 0:
    print(n)
    n = n - 1

print("Happy birthday")

# The flow of the execution of a while statement:
# 1. Evaluate the condition, yielding True or False
# 2. If the ocndition is false, exit the while statement and continue execution at the next statement
# 3. If the condition is true, execute the body and then go back to step 1

# This type of flow is called a loop because the third step loops back around to the top. Each execution of the body is the loop is an interation
# The body of the loop should change the value of one or more variables so eventually the condition becomes false and the loop terminates.
# The variable that changes each time the loop executes and controls when the loop is finished is called the iteration variable
# Loops without an interation variable are infinite loops

####################################################################################################################################################################
# 5.3 Infinite loops
####################################################################################################################################################################
# Infinite loops have no iteration variable and go on forever, since there is no ending condition
# These loops can be useful when the duration of execution is unknown. In these cases an infinite loop can be written and can use a break statement to jump out of the loop

# The following loop is an infinite loop because the logical expression on the while statement is simply the logical constant True:

n = 10
while True:
  print(n, end = " ")
  n = n -1
print("Done!")

# This code will run until the user types "done"

while True:
  line = input('> ')
  if line == 'done':
    break
  print(line)
print('Done!')

# The loop condition is true, which is always true, so the loop runs repeatedly until it hits the break statement

####################################################################################################################################################################
# 5.4 Finishing Iterations with continue
####################################################################################################################################################################
# Occasionaly, it is neccessary to finish the current iteration of the loop and to immediately jump to the next iteration
# In this case use the continue statement to skip to the next iteration without finishing the body of the for loop for the current iteration

while True:
    line = input('> ')
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done")

# The following code copies the input its user provides unless the input starts with "#". The loop ends when the input is "done"
# All lines are printed except the one the starts with hash sign because when the continue is executed, it ends the current iteration and jumps back to the while statement to start the next iteration

####################################################################################################################################################################
# 5.5 Definite loops using for
####################################################################################################################################################################
# Sometimes loops are used to loop through a set of things such as a list of words, line, or list of numbers
# These types of loops are definite loops that are constructed using a for statement
# # For loops are definite loops because they are looping through a known set of items for as many iterations as there are items in the set

friends = ["Kiki", "Marsey", "Carp"]
for friend in friends:
    print("Happy New Year:", friend)
print("Done")

# The loop will go through three iterations because there are three items in the list
# friend is an iteration variable for hte loop, it changes for each iteration of the loop and controls when the for loop completes. The iteration variable successively through the three strings stored in the friends variable

####################################################################################################################################################################
# 5.6 Loop Patterns
####################################################################################################################################################################
# Often time for or while loops are used to go through a list of items or the contents of a file to look for the largest or smallest value of the data
# These loops ar egenerally constructed by:
# 1. Initializing one or more variables before the loop starts
# 2. Performing some computation on each item in the loop body, possibly changing the variables in the body of the loop
# 3. Looking at the resulting variables when the loop completes

####################################################################################################################################################################
# 5.6.1 Counting and Summing Loops
####################################################################################################################################################################
# Example looop:

count = 0
for itervar in [3, 44, 12, 9, 74, 15]:
    count = count + 1
print("Count:", count)

# The following loop counts the number of items in a list. For each iteration of the loop the count variable increases by one

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print("Total:", total)

# This loop uses the iteration variable. The loop adds up all of the sum of the elements; a variable used this way is sometimes called an accumlator

####################################################################################################################################################################
# 5.6.2 Maximum and minimum loops
####################################################################################################################################################################

largest= None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop:", itervar, largest)
print("Largest:", largest)

# The loop above finds the largest value in a list or sequence
# The variable largest is best thought of as the "Largest value we have seen so far"
# Before the loop, largest is set to the constant None. None is a special constant value which can store a variable to mark the variable as "empty"

# The following is a simple version of the Python built-in min() function:

def min(values):
  smallest = None
  for value in values:
    if smallest is None or value < smallest:
      smallest = value
return smallest

####################################################################################################################################################################
# 5.9 Exercises
####################################################################################################################################################################
# 1. Write a program which repeatedly reads numbers unti the user enters "done". Once "done" is entered, print out the totla, count and average of the numbers.
# If the user enters anything other than a number, detect their mistakes using try and except and print an error message and skip to the next number

count = 0
total = 0
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        else:
            num = int(num)
            count = count + 1
            total = num + total
            continue
    except:
        print("Invalid input")
        continue
print(total, count, total/count)

# 2. Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

min = None
max = None
while True:
    num: str = input("Enter a number: ")
    try:
        if num == "done":
            break
        else:
            num = int(num)
        if min is None or min > num:
                min = num
        if max is None or max < num:
                max = num
        continue
    except:
        print("Invalid input")
        continue
print(min, max)

####################################################################################################################################################################
# End Of Chapter 5
####################################################################################################################################################################








