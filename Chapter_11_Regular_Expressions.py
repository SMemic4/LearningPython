####################################################################################################################################################################
# Chapter 11: Regular Expressions
####################################################################################################################################################################
# 11.0 Regular Expressions
####################################################################################################################################################################
# The task of searching and extracting is so common that python has a very powerful module called regular expressions that handles many of these tasks elegantly
# Regular expressions are almost their own programming language for searching and parsing strings
# The regular expression module re must be imported into a program before it can be used
# THe simplest use of the regular expression module is the search() function

import re 
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line) # Searches and prints for lines that contain "From"
        
# The line could have also been used with line.find()

# The power of regular expressions comes from when adding special characters to search strings that allow for a more precisely controled match with lines
# Adding these special character to regular expression allows for sophisticated matching and extraction while writing little code

# For example, the carat character is used in regular expressions to match "the beginning" of a line. 
# The program above could be changed to match lines only where "From:" was at the beginning of the line as follows:

import re 
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line) # Searches and prints for lines that contain "From"

# This will only match lines that start with the string "From:"

####################################################################################################################################################################
# 11.1 Character Matching in Regular Expressions
####################################################################################################################################################################

