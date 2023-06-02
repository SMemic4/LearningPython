####################################################################################################################################################################
# Chapter 6: Strings
####################################################################################################################################################################
# 6.1 A string is a sequence
####################################################################################################################################################################
# A string is a sequence of characters. Characters can be accessed one at a time with the bracket operator

fruit = "banana"
letter = fruit[1]
print(letter) # a

# The second statement extracts the character at index position 1 from the fruit variable and assigns it to the letter variable
# The expression in brackets is called an index. THe index indicates which charcter is selected in the sequence
# Note the in python, the index is an offset from the beginning of the string, and the offset of the first letter is zero

letter = fruit[0]
print(letter) # b

# Any expression, including varaibles and operators can be used as an index, but the value of the index has to be an integer otherwise an error occurs

letter = fruit[1.5] # TypeError: string indices must be integers

####################################################################################################################################################################
# 6.2 Getting the length of a string using len
####################################################################################################################################################################
# len is a built-in function that returns the number of characters in a string

fruit = "apple"
len(fruit)

# Negative indicees can be used, which count backawards from the end of the string

fruit[-1] # prints e

####################################################################################################################################################################
# 6.3 Traversal through a string with a loop
####################################################################################################################################################################
# A lot of computations involve processing a string one character at a time.
# Ofthen they start at the beginning, select each character in turn, do something to it and continue until the end. 
# This pattern of processing is called a traversal

fruit = "apple"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    
# The loop traverses the string and displays each letter on a line.
# When the index is equal to the length of the string the condition is false and the body of the loop is not executed and ends

# Exercise 1. Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line except backwards

fruit = "apple"
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1

####################################################################################################################################################################
# 6.4 String slices
####################################################################################################################################################################
# A segement of a string is called a slice. Selecting a slice is similar to selecting a character:

s = "Kiki the cat"
print(s[0:5]) # kiki
print(s[5:12]) # the cat

# The operator [n:m] returns the part of the string from the "n-th" character to the "m-th" character, including the first but excluding the last
# If you omit the first index (before the colo), the slice starts at the beginning of the string If you omit the second index, the slice goes to the end of the string

fruit = "apple"
fruit[:3] # app
fruit[3:] # le

# If the first index is great than or equal to the second the result is an empty string represented by two quotation marks

fruit[3:3] # ""

# An empty string contains no character and has a length 0, but other than that, it is the same as any other string

# Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# it prints the entire string

fruit[:]

####################################################################################################################################################################
# 6.5 Strings are immutable
####################################################################################################################################################################
# It is tempting to use the operator on the left side of an assignment with the intention of changing a character in a string

greeting = "Hello world"
greeting[0] = "J" # TypeError: 'str' object does not support item assignment

# The object in this case is the string and the item is a character is being assigned
# An object is the same thing as a value. An item is one of the value in a sequence

# The reason for the error is that strings are immutable, meaning that an existing string can't be changed. The best thing to be done is to create a new string that is a variation of the original

greeting = "Hello world"
new_greeting = "JJJ" + greeting[1:]
print(new_greeting) # JJJello, world

# This example concatenates a new firt letter onto a slice of greetin, It has no effect on the original string

####################################################################################################################################################################
# 6.6 Looping and counting
####################################################################################################################################################################
# The following program counts the number of times the letter "a" appears in a string:

word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
print(count) # 3

# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(word, char):
    num = 0
    for letter in word:
        if letter == char:
            num = num + 1
    print(num)
    
####################################################################################################################################################################
# 6.7 The in operator
####################################################################################################################################################################
# The word in is a boolean operator that takes two string and returns True if the first appears as a substring in the second

print("a" in "cat") # True
print("b" in "cat") # False

####################################################################################################################################################################
# 6.8 String Comparison
####################################################################################################################################################################
# The comparison operators work on strings
word = "banana"
if word == "banana":
    print("It's the same word")

# Other comparison operations are useful for putting words in alphabetical order:

if word < "banana":
    print("Your word," + word + " comes before banana")
elif word > "banana":
    print("Your word," + word + " comes after banana")
else: 
    print("It's bananas")

# Python does not handle uppercase and lowercase letters the same way that most do. Al the uppercase letters come before the lowercase letters

word = "Pineapple"
if word < "banana":
    print("Your word," + word + " comes before banana")
elif word > "banana":
    print("Your word, " + word + " comes after banana")
else: 
    print("It's bananas") # Your word,Pineapple comes before banana

# A common way to address this problem is to convert strings to a standard format such as all lowercase, before performing the comparison

####################################################################################################################################################################
# 6.9 String Methods
####################################################################################################################################################################
# Strings are an example of python objects. An object contains both data and methods, which are functions that are built into the object and are available to any instance of the object
# Pyhtong has a function called dir which lists the methods available for an object
# The type function shows the type of function, while dir function shows the available methods

obj = "Kiki the cat"
type(obj) # <class 'str'>
dir(obj) # A list of functions
help(str.capitalize) # help() takes a function as an argument and returns a description of what the function does

# Calling a method is similar to calling a function (it takes arguments and returns a value), however the syntax is different.
# A method is called by appending the method name to the variable name using the period as a delimiter
# For example, the method upper takes a string and returns a new string with all uppercase letters
# Instead of the function syntax upper(word), it uses the method syntax word.upper()

word = "banana"
new_word = word.upper()
print(new_word) # BANANA

# The form dot notation specifies the name of the method, upper, and the name of the string to apply the method to, word/ The empty parenthese indicate that this method takes no argument
# A method call is called an invocation; in this case, upper is being invoked on the word
# For example, there is a string method named find that searches for the position of one string within another

word = "banana"
index = word.find("a")
print(index) # 1

# The find method can find substrings as well as characters

word.find("na") # 2

# It cn take a second argument of where the index should start:
 
word.find("na", 3) # 4

# One common task is to remove white space (spaces, tabs, or newlines) from the beginning and end of a string using the strip method

line = " That cat is oranage "
line.strip() # 'That cat is oranage'

# Some methods such as startswith returns boolean values

line = "Marsey the cat"
line.startswith("Marsey") # True
line.startswith("m") # False

# startswith requires case to math, so sometimes it is valuable to take the line and map it all to lowercase before doing any checking using the lower method

line = "Marsey the cat"
line.startswith("m") # False
line.lower().startswith("m") # True

# In the example above, the method lower is called and then startswith is used to see if the resulting lowercase string starts with the letter "m"

####################################################################################################################################################################
# 6.10 Parsing Strings
####################################################################################################################################################################








