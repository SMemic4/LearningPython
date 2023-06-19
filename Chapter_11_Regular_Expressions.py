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
# There are a number of ohter special characters that allow for the creation of even more powerful regular expressions. 
# The most commonly used special character is the period or full stop, which matches any character.
# In the following example, the regular expression F..m would match any of the strings "From:", "Fxxm:", "F11m:", or "F!@m"
# This is due to period characters in the regular expressiom matching any characters 

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# This is particularly powerful when combined with the ability to indicate that a character can be repeated any number of tiems using the * or + characters in a regular expression
# THese special characters mean that instead of matching a single character in the search string, they match zero-or-more characters (in the case of the *) or one-or-more character (int the case of the plus sign *)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:.+@', line):
        print(line)

# The search string '^F..m:.+@' will succesffuly search from lines that start with From and have an @ sign
# The .+ can be thought of as expanding to match all the character between the colon character and the at-sign 
# It is a good idea to think of the plus and asterisk character as pushy
# For example the following string would match the last at sign in the string as the .+ pushes outwards
# From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu
# It is possible to tell an asterisk or plus sign not to be so "greedy" by adding another character. Detailed documentation provides more infomation for turning of this behavior

####################################################################################################################################################################
# 11.2 Extracting Data using regular expressions
####################################################################################################################################################################
# To extract data from a stirng python, the findall() method can be used to extract all of the substrings which matches a regular expression
# The following program uses findall() to find the lines with email addresses in them and extracts one or more addresses from each of those lines

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
les = re.findall('\S+@\S+', s)
print(les) # ['csev@umich.edu', 'cwen@iupui.edu']

# The findall() method searches the string in the second argument and returns a list of all of the strings that look like email addresses
# Using a two-character sequence that matches a non-whitespace character (\S)
# Translating the regular expression, it searches for substrings that have at least one non-whitespace character, followed by an @ sign followed by at least one more non-whitespace character
# \S matches as many non-whitespace characters as possible
# The regular expression would match twice ['csev@umich.edu', 'cwen@iupui.edu'] but it would not match the string "@2PM" because there are no non-blank characters before the at sign
# Regular expressions in a program can be used to read all the lines in a file and print out anything that looks like an email address as follows: 


