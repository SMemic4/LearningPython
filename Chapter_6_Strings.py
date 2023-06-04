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
# Often times it will be neccesarry to look into a string and find a substring.
# For example if presented a series of lines formatted as follows:

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# And one wanted to pill out only the second half of the address, this can be done using find and string slicing
# First, the position of the at-sign will be found in the string, and then the position of the first space after the at-sign. Then string slcing will be used to extract the portion of the string

atpos = data.find("@")
print(atpos) # 21
sppos = data.find(" ", atpos)
print(sppos) # 31
host = data[atpos+1:sppos]
print(host) # uct.ac.za

# A version of the find method allows for a specific position to be specified where the string will begin to looking.

####################################################################################################################################################################
# 6.11 Format Operator
####################################################################################################################################################################
# The format operator (%) allows for the construction of strings, replacing parts of the strings with the data stored in variables
# When applied to integers % is the modulus operator, But when the first operand is a string % is the format operator
# For example, the format sequence %d means that the sewcond operand should be formatted as an integer ("d" stands for decimal)

camels = 42
print("%d" % camels) # 42

# The result is the string "42" which should not be confused with the integer value 42
# A format sequence can appear anywhere in the string, so a value can be embed in a sentence

print("I have spotted %d camels" % camels) # I have spotted 42 camels

# If there is more than one format equence in the string, the second argument has to be a tuple. Each format sequence is matched with an element of the tuple, in order.
# The following example uses %d to format an integer, %g to format a floating-point number, and %s to format a string 

print("In %d years I have spotted %g %s" % (3, 0.2, "camels")) # In 3 years I have spotted 0.2 camels

# The number of elements in the tuple must match the number of format sequences in the string. The types of the elements also must match the format

print("%d %d %d " % (1,2)) # TypeError: not enough arguments for format string
print("%d %d %d " % (1,2, 3)) # 1 2 3

# In the first example, there aren't enough elements; in the second, the element is the wrong type
# The format operator is powerful, but it can be difficult to use

# A tuple is a sequence of comma-separated values inside a pair of parenthesis

####################################################################################################################################################################
# 6.14 Exercises
####################################################################################################################################################################
# 1. Take the following python code that stores a string. Use find and string slicing to extract the portion of the string after the colo character and then use the float function to convert the extracted string into a floating point number

str = 'X-DSPAM-Confidence:0.8475'

beg = str.find(":")
sil = str[beg+1:]
sil = float(sil)
print(sil)

# 2. Read the documentation for string methods and experiment with them
# str.capitalize() returns a copy of a string with its first character capitalized and the rest lowercased 

word = "mArsey"
print(word.capitalize()) # Marsey

# str.casefold() returns a casefolded copy of the string

word = "MArsey"
print(word.casefold()) "marsey"

# str.count(sub, [,start[,end]]) return the number of non-verlapping occurences of a substring sub in the range [start,end]. Optional arguments start and end are intepred as in slice notation

word = "Marsey the cat is a cute cat and is an orange cat"
word.count("cat") # 3

# str.endwith(suffix{, start[, end]]) returns true if the string ends with the specified suffix otherwise returns false. suffix can also be a tuple of suffixes to look for

word = "That kitten is a cutie"
word.endswith("ie") # True
word.endswith("cuty") # False

# str.find(sub[, start[, end]]) returns the lowest index in the string where the substring sub is found with the slice. Returns -1 if sub is not found

word = "Kiki is a cute white cat"
word.find("white") # 15
word.find("ke") # -1

# str.index(sub[, start[, end]]) like find() but raises ValueError when the substring is not found

word = "Kiki is a cute white cat"
word.index("white") # 15
word.index("ke") # ValueError: substring not found

# str.isalnum() Returns True if all character in the string are alphanumeric and there is at least one character

word = "abcdefgh"
word.isalnum() # True

# str.islower() returns True if all cased characters in the string are lowercase and there is at least one cased character

word = "Marsey"
word2 = "marsey"
word.islower() # False
word2.islower() # True

# str.isnumeric() returns True if all characters in the string are numeric character and there is at least one character

word = "12345"
word2 = "1234aaaa"
word.isnumeric() # True
word2.isnumeric() #False

# str.isalnum returns TRUE if all characters in the string are alphanumeric (letters and numbers) and there is at least one character

word = "abcdef"
word2 = "asd12!3"
word.isalnum() # True
word2.isalnum() # False

# str.isatitle() returns True if the string is a titlecased string and there is at least one character, Uppercase character may only follow uncased characters and lowercase characters only cased ones

# str.isupper() returns True if all cased cahracter in the string are uppercase and there is at least one cased character

word = "MARSEY"
word2 = "kik"
word.isupper() # True
word2.isupper() # False

# str.lower() returns a copy of the string with all the cased characters converted to lowercase

word = "KIKI"
word.lower() # 'kiki"

# str.partiion(sep) splits the string at the first occurrrence of spe, and returns a 3-tuple containing the part beofre the separator and the separator itself

word = "Marsey the cat"
word.partition("the")

# str.removeprefix() if the string starts with the prefix string, reutnrs string{len(prefix)}, otherwise return a copy of the string

word = "Marsey the cat"
word.removeprefix("Marsey") # " the cat"

# str.removesuffix() if the string ends with the suffix string, returns string{len(prefix)}, otherwise return a copy of the string

# str.replace(old, new[, count]) returns a copy of the string with all occurrences of substring old replaced by new. 

# str.split(sep=None, maxsplit=- 1) returns a list of words in the string, using sep as the delimiter string. 

####################################################################################################################################################################
# End of Chapter 6
####################################################################################################################################################################








