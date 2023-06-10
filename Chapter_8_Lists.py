####################################################################################################################################################################
# Chapter 8: Lists
####################################################################################################################################################################
# 8.1 A List is a Sequence
####################################################################################################################################################################
# Like a string, a list is a sequence of values. In a string the values are character; in a list they can be any type
# Thevales in lists are called elements or items
# There are several ways to create a new list; simplest is to enclose the elements in square brackets []

[10,20,30,40] # Example of a list of four integers
['orange', 'cat', 'cute'] # Example of a list with three strings

# Elements in a list don't have to be the same type, and can even contain other lists

['spam', 2.0, 5, [10, 20]] # Example of a list which elements are a string, float, integer, and another lists

# A list within another list is nested
# A list that contains no elements is called an empty list; one can be created with empty brackets[]
# Lists can be assigned to variables

cats = ["marsey", "kiki", "Tuby"]
numbers = [17, 123]
empty = []
print(cats, numbers, empty) # ['marsey', 'kiki', 'Tuby'] [17, 123] []

####################################################################################################################################################################
# 8.2 Lists are Mutable
####################################################################################################################################################################
# The syntax for accessing the elements of a list is the same for accessing the character of a string: the bracket operator
# The expression insde the brackets specifie the index (Remeber that indicies start at 0):

print(cats[0])

# Unlike strings, lists are mutable because the order of items in a list can be changed or reassigned
# When the bracket operator appears on the left side of an assignment, it identifies the elements of the lists that will be assigned

numbers = [17, 123]
numbers[1] = 5
print(numbers) # [17, 5]

# Lists can be thought of as a relationship between indices and elements. This relationship is called a mapping; each indexx "maps to" one of the elements
# List indices work the same way as string indices:
# Any integer expression can be used as an index
# Trying to read or write an element that does not exist, gives an IndexError
# If an index has a negative value, it counts backwards from the end of the list 

# The in operator also works on lists

cats = ["marsey", "kiki", "Tuby"]
"marsey" in cats # True
"Chuddy" in cats # False

####################################################################################################################################################################
# 8.3 Travesing a List
####################################################################################################################################################################
# The most common way to tranverse the elements of a list is with a for loop. It follows the same syntax as for string

cats = ["Marsey", "kiki", "Tuby"]
for cats in cats:
    print(cats)

# THis works well for reading the elements of the list. But to write or update the elements, indices are required
# A common way to do this is to combine the functions range and len:

cats = ["Marsey", "kiki", "Tuby"]
numbers = [1, 2, 3, 4, 5, 10]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers) # 2, 4, 6, 8, 10, 20

len(numbers)
range(len(numbers))

# The loop traverses the list and updates each element.len returns the number of elements in the list
# range returns a list of indicesfrom 0 to n-1, where n is the length of the list

# A for loop over an empty list never executes the body:
 
empty = []
for x in empty:
  print("This never happens")

# Although a list can contain another list, the nested list still counts as a single element. The length of this is four

lss = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
len(lss) # 4


####################################################################################################################################################################
# 8.4 List Operations
####################################################################################################################################################################
# The + operator concatenates lists:

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]

# Similarly, the * operator repeats a list a given number of times:

print([0] * 4) # [0, 0, 0, 0] Repeats the list four times
print([1, 2, 3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] Repeats the list three times

####################################################################################################################################################################
# 8.5 List Slices
####################################################################################################################################################################
# The slice operator also works on lists:

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] # ['b', 'c']
t[:4] # ['a', 'b', 'c', 'd']
t[3:] # ['d', 'e', 'f']
t[0:3] # ['a', 'b', 'c']
t[0:5]
v = [1, 2, 3, 4, 5, 6]
v[0] # 1 
v[1] # 2
v[1:3] # 2, 3
v[1:] # 2, 3, 4, 5, 6
v[:4] # 1, 2, 3 ,4

# Omitting the first index will cause the slice to start at the beginning. Omitting the second, the slice goes to the end. Omitting both gives a copy of the whole list

t[:] # ['a', 'b', 'c', 'd', 'e', 'f']

# Since lists are mutable, it is often useful to make a copy before performing operations that fold spince, or mutilate lists
# A slice operator on the left side of an assignment can update multiple elements:

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ["x", "y"]
print(t) # ['a', 'x', 'y', 'd', 'e', 'f']

####################################################################################################################################################################
# 8.6 List Methods
####################################################################################################################################################################
# Python provides methods that operate on lists. For example, append adds a new element to the end of a list

t = ["a", "b", "c"]
t.append("d")
print(t) # ['a', 'b', 'c', 'd']

# Extend takes a list as an argument and appends all of the elements:

t1 = ["a", "b", "c"]
t2 = ["d", "e"]
t1.extend(t2)
print(t1) # ['a', 'b', 'c', 'd', 'e']

# The example above leaves t2 unmodified

# sort arranges the elements of the list from low to high:

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t) # ['a', 'b', 'c', 'd', 'e']

# Most list methdods are void; they modify the list and return None. Writing t= t.sort() will provide disappointing results

####################################################################################################################################################################
# 8.7 Deleting Elements
####################################################################################################################################################################
# There are several ways to delete elements from a list. If the index of the element is known, then the method pop() can be used

t = ['a', 'b', 'c']
x = t.pop(1)
print(t) # ['a', 'c']
print(x) # b

# pop() modifies the list and returns the element that was removed. If an index isn't provided, it deletes and returns the last element 
# If the removed value is unneeded, then use the del statement()

t = ['a', 'b', 'c']
del t[1]
print(t) # ['a', 'c']

# If the element is known but not it's indice is knwon, the method remove() will take a value and remove it from the list. The return value from remove is none

t = ['a', 'b', 'c']
t.remove("b")
print(t) # ['a', 'c']

# To remove more than one element, use del with a slice index

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t) # ['a', 'f']

# As usual, the slice selects all the elements up to, but including the second index

####################################################################################################################################################################
# 8.8 Lists and Functions
####################################################################################################################################################################
# There are a number of built-in functions that can be used on lists that allow for quick iteration through lists without writing loops:

nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # 6
print(max(nums)) # 74
print(min(nums)) # 3
print(sum(nums)) # 154
print(sum(nums)/len(nums)) # 25.6666

# The sum() functions only works when the list elements are numbers
# The other functions (max(), len(), etc) works with lists of strings and other types that can be comparable
# Here is a function that computes an avaerage without a list:

total = 0
count = 0
while (True):
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count = count + 1
average = total /count
print("Average:", average)

# However, it's more simple to remember each number the user entered and use built-in functions to compute the sum and count at the end

numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print("Average:", average)

# This method requires an empty list before the loop starts, and then each time a number is entered to append it to the list
# At the end of the program, the sum is computed and divide by the count of the list to create an average

####################################################################################################################################################################
# 8.9 Lists and Strings
####################################################################################################################################################################
# A string is a sequence of characters and a list is a sequence of values, but a list of character is not the same as a string. To  convert from a string to a list of characters use list()

s = "snakes"
t = list(s)
print(t) # ['s', 'n', 'a', 'k', 'e', 's']

# Because list is the name of a buily-in function avoid using it as a variable name
# The list function breaks a string into individual letters. To break a string into words, use the split method:

s = 'Marsey is a cute cat'
t = s.split()
print(t) # ['Marsey', 'is', 'a', 'cute', 'cat']
print(t[4]) # cat

# After split is used to break the string into a list of words, the index operator (square bracket) to look at a particular word in the list
# Split can be called with an optional argument called a delimiter that specifies which characters to use as word boundaries

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)  # ['spam', 'spam', 'spam']

# join is the inverse of split. It takes a list of strings and concatenates the elements. 
# join is a string method, so to invoke it, it must be passed with a delimiter

t = ["kiki", "is", "a", "cute", "cat"]
delimter = " "
delimter.join(t) # 'kiki is a cute cat'

# In this case the delimiter is a space character, so join puts a space between words
# To concatenate strings without spaces, use an empty string "" as a delimiter

####################################################################################################################################################################
# 8.10 Parsing Lines
####################################################################################################################################################################
# Usually when reading a file, it is often that case there is a need to do something to the line rather than just reading it
# THis includes parsing the line to find interesting parts of the line
# Imagine wanting to print out the day of the week from the lines that start with "From":
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# The split method is effective for this type of problem. 
# Write a samll program that looks for lines where the line starts with "From", split those lines and then print out the third word

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    print(words[2])
    
####################################################################################################################################################################
# 8.11 Objects and Values
####################################################################################################################################################################
# Execute the following assinment statements

a = "kiki"
b = "kiki"

# Both a and b both refer to a string, but it is not known if they refer to the same string
# To check whether two variables refer to the same object, use the is operator

a is b # True

# In this example, python only created one string object, and both a and b refer to it
# But, when you create two lists, two objects are created

a = [1, 2, 3]
b = [1, 2, 3]
a is b # False

# In this case, the two lists are equivalent because they have the same elements, but not identical because they are not the same object. 
# IFt two objects are identical, they are also equivalent, but if they are equivalent, they are not necessarily identical 
# Object and value are used interchangeably, but it is more precise to say than an object has a vlaue
####################################################################################################################################################################
# 8.12 Aliasing
####################################################################################################################################################################
# IF a refers to an object and b is assinged to a (b = a) than both variables refer to the same object

a = [1, 2, 3]
b = a
b is a # True

# The association of a variable with an object is called a reference. In this example, there are two references to the same object
# An object with more than one reference has more than one name, this is refered to the object being aliased
# IF the aliased object is mutable, changes made with one alias affects the other

b[0] = 17
print(a) # [17, 2, 3]

# Athought this behavior can be useful, it is error-prone, In general, it is safer to avoid aliasing when working with mutable objects
# For immutable objects like strings, aliasing is not as much of a problem

####################################################################################################################################################################
# 8.13 List Arguments
####################################################################################################################################################################
# When passing a list to a function, the function gets a reference to the list
# If the function modifies a list parameter, the caller sees the change:

def delete_head(t):
  del t[0]
  
letters = ["a", "b", "c"]
delete_head(letters)
print(letters) # ['b', 'c']

# The parameter t and the variable letters are aliases for the same object
# It is important to distinguish between operations that modify lists and operations that create new lists
# For example, the append method modifies a list, but the + operator creates a new list:

t1 = [1, 2]
t2 = t1.append(3)









