####################################################################################################################################################################
# Chapter 9: Dictionaries
####################################################################################################################################################################
# 9.0 Introduction
####################################################################################################################################################################
# A dictionary is like a list, but more general. In a list, the index positions have to be integers; in a dictionary, the indices can be (almmost) any type
# A dictionary can be thought of as a mapping between a set of indices (called keys) and a set of values
# Each key maps to value. The association of a key and a value is called key-value pair or sometimes an item 
# As an exmaple, a dictionary that maps from English to Spanish words will be built, so that all keys and values are all strings

# The function dict creates a new dictionary with no items. Because dict is the name of a built0in function , avoid using it as a variable name

eng2sp = dict()
print(eng2sp) # {}

# The curly brackets [], represent an empty dictionary
# To add itmes to the dictionarny, square brackets are used

eng2sp["one"] = "uno"
print(eng2sp) # print(eng2sp)

# The line above creates an item that mapes from the key "one", to the value "uno". Printing the dictionary shows the key-value pair with a colon between the key and value
# The output format is also an input format.
# For example, creating a ne wdictionary with three items and printing it provides a suprise

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp) # {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# The order of the key-value pairs may not be in the correct order. In general, the oreder of items in a dictionary is unpredictiable
# But that's not a problem because the elements of a dictionary are never indexed with integer indicies. Instead keys are used to look up corresponding values

print(eng2sp["two"]) # dos

# The key "two" always maps to "dos" so the order of items doesn't matter
# If the key isn't in the dictionary an exception occurs

print(eng2sp["four"]) # KeyError: 'four'

# THe len function works on dicitionaries, it returns the number of key-value pairs

len(eng2sp) # 3

# The in operator works on dicitionaries, it tells you whether something appears as a key in the dictionary (appearing as a value is not good enough)

"two" in eng2sp # True
"dos" in eng2sp # False

# To determine whether something appears as a value in a dictionary, the values method can be used, which returns the values as a type that can be converted to a list and then used in the in operator

vals = list(eng2sp.values())
'uno' in vals # True

# The in operator uses different algorithms for lists and dictionaries. 
# For lists, it uses a linear search algorithm. As the list gets longer, the search time gets longer in direct proportion to the length of the list
# For dictionaries, Pyhton uses an algorithm called a has table that has a remarkable property: the in operator takes the same amount of time no matter how many items there are in a dictionary

# Exercise 1.  Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the dictionary.

fhand = open("words.txt")
words = dict()
n = 0
for lines in fhand: 
    lines = lines.rstrip()
    spt = list(lines.split(" "))
    for i in spt:
        words[i] = n
        n += 1
        
print(words)
vals = list(words.values())
print(23 in vals)

####################################################################################################################################################################
# 9.1 Dictionary as a set of counters
####################################################################################################################################################################
# Suppose there is a task of being given a string and count how many times each letter appears. THere are several ways this can be done
# 1. Create 26 variables, one for eahc letter of the alphabet. THen traverse the string and for each character increment the corresponding counter, using a chained conditional
# 2. Create a list with 26 elements, then converting each character to a number (using the built-in function ord), use the number as an index into the list, and increment the approiate counter
# 3. Create a dictionary with characters as keys and counters as the corresponding values. The first time a characher is een, it would be added as an item to the dictionary. After that the value of the item would be ipdated
# Each of these options performs the same computation, but each of them implements that computation in a different way
# An implementation is a way of performing a computation; some implementations are better than others
# An advantage of the dictionarary implementation is that that letters don't need to be known ahead of time and that letters are only made for the values that appear in strings
# Here's an example of what the code might look like:

word = "brontosaurus"
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else: 
        d[c] = d[c] + 1
print(d) # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

# The code effectively becomes a computing histogram, which is a statistical term for a set of counters (or frequencies)
# The for loop traverses the stirng. Each through the loop, if the character c is not in the dictionary, a new item is creted with key c and the intial value 1
# If c is alraedy in the dictionarray the value is incremented by one using d[c]
# The histrogram indicates taht the letters "a" and "b" appear once, while "o" appears twice and so on 

# Dictionaries have a method called get that takes a key and a default value. If the key appears in the dictionary, get returns the crresponding value otherwise it returns the default value 

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0)) # 100
print(counts.get('tim', 0)) # 0

# Get can be used to write the histogram loop more concisely. Because the get method automatically handles the case where a key is not in a dictionarary
# It can be reduced four lines down to one and eliminate the if statemnet:

word = "brontosaurus"
d = dict()

word = "brontosaurus"
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d) # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
 
# The use of the get method to simplify this counting loop ends up being a very commonly used "idiom" in Python and will be used many times in code

####################################################################################################################################################################
# 9.2 Dictionaries and Files
####################################################################################################################################################################
# One of the common uses of a dictionary is to count the occurrence of words in a file with some wrriten text
# Start with a simple file of words taken from the text Romemo and Juliet in romeo.txt
# A ython program will be written that will read through the lines of the file, break each line into a list of words, and then loop through eac of the words in the line and add count each word using a dictionary
# Two loops will be needed. The outer loop is reading the lines of the file while the inner loop is iterating through eac of hte words on that particular line
# This is an example of a pattern called nested loops
# Because the inner loop executes all of its iterations each time the outer loop makes a single iteration. the inner loop can be thought of iterating "more quickly" and the outer loop more slowly

fhand = open("romeo.txt")
d = dict()
for lines in fhand:
    words = lines.split()
    for c in words:
        d[c] = d.get(c,0) + 1
        
print(d)

####################################################################################################################################################################
# 9.3 Looping and Dictionaries
####################################################################################################################################################################
# Using a dictionary as the sequence in a for statement, it traveses the keys of hte dictionary. This loop prints each key and the corresponding value

count = {'kiki' : 1, 'marsey' : 2, 'capy' : 3 }
for key in count:
    print(key, count[key])
    
# kiki 1 marsey 2 capy 3

# They keys don't have to be in any particular order
# This pattern can be used to implement the various loop idioms described earlier. For example finding  all entires in a dictionary with a value above ten 

count = {'kiki' : 1, 'marsey' : 200, 'capy' : 300 }
for key in count:
    if count[key] > 10: 
        print(key, count[key])  # marsey 200 capy 300

# The for loop iterates through the keys of the dicitionaray, so the index operator must be used to retrieve the corresponding value for each key

# To print the keys in alphabetical order, first make a list of the keys in the dictionary in the dictionary using the keys method avaiable in dictionary objects
# THen sort that list and loop through the sorted list, looking up each key and printing out key-value pairs in sorted order

counts = {'kiki' : 1, 'marsey' : 200, 'capy' : 300 }
les = list(counts.keys()) 
print(les) # ['kiki', 'marsey', 'capy']
les.sort()
print(les) # ['capy', 'kiki', 'marsey']
for key in les:
    print(key, counts[key]) # capy 300 kiki 1 marsey 200

# This sorts the list of keys-value pairs in order

####################################################################################################################################################################
# 9.4 Advanced Text Parsing
####################################################################################################################################################################
# In the above example, ising the file romeo.txt the file was made as simple as possible by removing all punctuation by hand. The actual text has losts of puncatuation

# Since the python split function looks for spaces and treats words and treats words as tokens separated by spaces it would treat words like "soft" and "soft!" as different words and thus create a separate dictionary entry for each word
# Additionally capitalization of words like "who" and "Who" are treated as different words with different counts

# These methods can be solved by using string methods lower, punctuation, and translate 
# The translate method is the most subtle of the methods. Here is the documentation for translate:
# line.translate(str.maketrans(fromstr, tostr, deletestr))
# Replace the characters in fromstr with the character in the same position in tostr and delete all characters that are in deletestr. 
# The fromstr and tostr can be empty strings and the deletestr parameter can be omitted.

# The deletestr parameter will be used to delte all of the punctuation
# Python will provide the list of characters that it cosniders punctuation:

import string
string.punctuation # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# The program will recieve the following modifications

import string
fhand = open("romeo-full.txt")
d = dict()
for line in fhand: 
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        d[word] = d.get(word, 0) + 1
print(d)

####################################################################################################################################################################
# 9.7 Exercises
####################################################################################################################################################################
# 1. Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines 
# that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

fhand = open("mbox-short.txt")
d = dict()
days = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith("From"):
        les = line.split()
        if len(les) > 3:
            for word in les:
                days.append(les[2])
                print(days)
                for day in days:
                    d[day] = d.get(day, 0) + 1
print(d)



# 2. Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

fhand = open("mbox-short.txt")
d = dict()
email = list()
for lines in fhand:
    if lines.startswith("From"):
        lines = lines.rstrip()
        lines = lines.split(" ", 1)
        for words in lines:
            email.append(lines[1])
            for add in email:
                d[add] = d.get(add, 0) + 1
print(d)




















