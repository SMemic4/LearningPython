####################################################################################################################################################################
# Chapter 10: Tuples
####################################################################################################################################################################
# 10.1 Tuples are Immutable
####################################################################################################################################################################
# A tuple is a sequence of values much like a list
# The values stored in a tuple can be any type and are indexed by integers
# THe important difference is that tuples are immutable
# Tuples are also comparable and hashable so they sort lists of them and use tuples as key values in python dictionaries
# Syntactically, a tuple is a comma-separated list of values:

t = 'a', 'b', 'c', 'd', 'e'

# Although it is not necessary, it is common to enclose tuples in parentheses to help quicklly identify tuples when looking at python code

t = ('a', 'b', 'c', 'd', 'e')

# To create a tuple with a single element, it must be included with a final comma:

t1 = ('a',)
type(t1) # <class 'tuple'>

# Without the comma python treats ('a') as an expression with a string in parentheses that evaluates to a string:

t2 = ("a")
type(t2) # <class 'str'>

# Another way to construct a tuple is the bult-in function tuple(), With no argument it creates an empty tuple:

t = tuple()
print(t) # ()

# If the argument is a sequnce (string, list, or tuple), the result of the call to tuple is a tuplpe with the lements of the sequence

t = tuple("lupins")
print(t) # ('l', 'u', 'p', 'i', 'n', 's')

# Because tuple is the name of a constructor, avoid using it as a variable name
# Most list operators also work on tuples. The bracket operator indexes an element:

t = ('a', 'b', 'c', 'd', 'e')
print(t[0]) # a 

# The slice operator selects a range of elements

print(t[1:3]) ('b', 'c')

# Modifying one of the elements of a tuple provides an error:

t[0] = "A" # TypeError: 'tuple' object does not support item assignment

# Elements of a tuple can't be modifyed but one tuple can be replaced with another

t = ("A",) + t[1:]
print(t) # ('A', 'b', 'c', 'd', 'e')

####################################################################################################################################################################
# 10.2 Comparing Tuples
####################################################################################################################################################################
# The comparison operator works with tuples and other sequences
# Python starts by comparing the first element from each sequence. If they are equal, it goes to the next element and so on, until it finds elemetns that differ
# Subsequent elemnts are not considered upon finding a prior difference

(0, 1, 2) < (0, 3, 4) # True
(0, 1, 200000000) < (0, 3, 4) # True

# Thew sort() function works the same way. it sorts primarily by first element, but in the case of a tie, it sorts by the second element and so on 
# This feature lends itself to a pattern called DSU for:
# Decorate a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence
# Sort the list of tuples using the python built in sort
# Undecorate by extracting the sorted elements of the sequence

# For example, suppose one has a list of words that need to be sorted from longest to shortest

txt = 'but soft what light in yonder window breaks'

words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

print(t) # [(3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (2, 'in'), (6, 'yonder'), (6, 'window'), (6, 'breaks')]
t.sort(reverse = True)
print(t) # [(6, 'yonder'), (6, 'window'), (6, 'breaks'), (5, 'light'), (4, 'what'), (4, 'soft'), (3, 'but'), (2, 'in')]

res = list() 
for length, word in t:
    res.append(word)
    
print(res) # ['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']

# The first loop builds a list of tuples, where each tuple is a word preceded by it's length
# sort compares the first element, length, first, and only considers the second element to break ties
# The keyword argument reverse = True tells sort to go in decreasing order

# The second loop traverse sthe list of tuples and builds a list of words in descending order of length. The four-character words are sorted in reverse alphabetical order

####################################################################################################################################################################
# 10.3 Tuples Assignment
####################################################################################################################################################################
# One of the unique syntactic features of the Python language is the ability to ahve a tuple on the left side and a sequence on the right side of an assignment statement
# This allows for the assignment of more than one variable at a time to a given ssequence

# This exmaple shows a two-elemnt list (which is a sequence) and assigns the first and second elemetns of the sequence to the varaibles x and y in a single statement

m = [ 'have', 'fun' ]
x, y = m
x # have
y # fun

#  Python rouglytranslates teh tuple assignment syntax to be the following 

m = [ 'have', 'fun' ]
x = m[0]
y = m[1]
x # have
y # fun

# Stylistically when using a tuple on the left side of the assignment statement, the parenthese are omitted, but the following is an equally valud syntax 

m = [ 'have', 'fun' ]
(x, y) = m
x # have
y # fun

# A particularly clever application of tuple assignment allows for the swaping of the values of two variables in a single statement 

a, b = b, a

# Both sides of the statement are tuples, but the left side is a tuple of variables; the right side is a tuple of expressions
# Each value on the right side is assigned to its respective variable on the left side
# All the ezpressions on the right side are evaluated before any of the assignments 

# The numbers of variables on the left and the number of values on the right must be the same otherwise an error occurs 

a,b = 1, 2 , 3 # ValueError: too many values to unpack (expected 2)

# More generally. the right side can be any kind of sequence (string, list, or tuple) 
# For example to split an email address into user name and a domain using the following code 

addr = "marsey@thecat.org"
uname, domain = addr.split("@")
print(uname) # Marsey
print(domain) # thecat.org

####################################################################################################################################################################
# 10.4 Dictionaries and Tuples
####################################################################################################################################################################
# Dictionaries have a method called items that reutrns a list of tuples where each tuple is a key-value pair:

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t) # [('a', 10), ('b', 1), ('c', 22)]

# However, since the list of tuples is a list, and tuples are comparable, the list of tuples can now be sorted
# Converting a dictionary to a list of tuples is way to output the contents of dictionary sorted by key: 

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
t # [('a', 10), ('b', 1), ('c', 22)]
t.sort(reverse = True)
t # [('c', 22), ('b', 1), ('a', 10)]

# The new list is sorted in descending order by the key value

####################################################################################################################################################################
# 10.5 Multiple Assignment with dictionaries
####################################################################################################################################################################
