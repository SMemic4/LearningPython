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

import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall("\S+@\S+", line)
    if len(x) > 0:
        print(x)

# Each line is read and then all the substrings that match the regular expression are extracted
# Since finall() returns a list, the number of elements in the list is check to find more than zero to print only lines where at least one substring was found

# Some of the email adddresses have incorrect characters like "<" or ";" at the beginning or end
# Regular expression can be used to exract the portion of the string that starts and ends with a letter or a number
# This requires using another feature of regular expressions
# Square brackets are ussed to indicate a set of multiple acceptable characters to match with
# Remember, \s is asking to match the set of "non-white space characters"
# Here is the new regular expression:
# [a-zA-Z0-9]\S*@\S*[a-zA-Z]
# The regular expression starts by looking for substrings thqt start with a single lowercase letter, uppercase letter, or number, followed by zero or more non-blank characcters (\S*)
# Followed by an at-sign, followed by zero or more non-blank characters (\S*) followed by an uppercase or lowercase letter
# The switch from + to * indicate zero or more non-blank character since  [a-zA-Z0-9] is already one non-blank character
# Remember that the * or + applies to the single character immediately to the left of the plus or asterisk

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
        
# The regular expression eliminated two letters at the end of the string (">")
# This is because when apeending [a-zA-Z] to the end of the regular expression demands wahatever string the regular expression aprser finds must end with a letter

####################################################################################################################################################################
# 11.3 Combining Searching and Extracting 
####################################################################################################################################################################
# To find numbers on the lines that start with the string "X-" such as:
# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000
# To extract any floating-point numbers that have the same syntax
# A regular expression can be used to select thesde lines:
# ^X-.*: [0-9.]+
# The regular expression above starts by looking for lines that start with X-, followed by zero or more charracter (.*), followed by a colon (:) and then a space
# After the space it looks for one or more characters that are either a digit (0-9) or a peiod [0-9.]+
# Note that inside teh square brackets, the period ,atches an actual period 

import re

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

# When running the program above, the data filters to show only the lines that are of interest
# However, now the issue is solving the problem of extracting the numbers
# While it would be simple enough to use split, there is another feature of regular expressions that both searches and parses the line at the same time. 

# Parentheses are another special character in regular expressions, when adding parentheses to a regular expression, they are ignored when matching the string
# But when using finall(), parenthese indicate to the code toee match the whole whole expression, but to only extract a protion of the substring that matches the regular expression

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

# Instead of calling search)_, parentheses are added as part of the regular expression that represnets the folating-point number to indicate to finall() to return the floating-point number portion of the matching string

# The code to extract all of the revisionnumbers (the integer number at the end of the lines)

import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('^Details:.*rev=([0-9]+)', line)
  if len(x) > 0:
    print(x)

# The regex, beings by looking for lines that start with Details: followed by an number of character (.*) followed by rev=, and then one or more digits
# This finds the lines that match the regular expression but only extracts the integer number at the end of the line 
# Remember that [0-9]+ is "greedy" and it tries to make as large a string ofd digits as possible before extracting those digits
# This greedy behavior is why all five digits for eahc numbers are extracted from eahc line
# The regular expression expands in both directions until it encounters a non-digit or the beginning or the end of a line


# To extract the hour of the day for each line from the previous exercises would use the following regular expression:
# ^From .* [0-9][0-9]:
# The translation of this regular expression is that it looks for lines that with From (note the space). followed by an number of chracter (.*), followed by a space, followed by two digits [0-9][0-9], followed by a colon charcter
# In order to pull out only the hour using findall(), add parenthesse around the two digits as follows: 
# ^From .* ([0-9][0-9]):

import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  x = re.findall('^From .* ([0-9][0-9]):', line)
  if len(x) > 0:
    print(x)

####################################################################################################################################################################
# 11.4 Escape Character
####################################################################################################################################################################
# Since special characters are used in regular expressions to match the beginning or end of a line or specifiy wild cards a method to indicate these characters are "normal" is needed
# THese are indicated by simply match a character by prefixing the character with a backslash

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x) # 12

# Since the dollar sign is prefixed with a backslash it asctually matches the dolloar sing ni the input string instead of matching the "end of line" and the rest of the regular expression matches one or more digits or the period character
# Note that inside square brackets, characters are not "special". When saying [0-9] it really means digits or a period. Outside of square bracets a period is the wildcard character and matches any character. Inside square brackets it's simply a period

####################################################################################################################################################################
# 11.5 Summary
####################################################################################################################################################################
# There are search strings with special characters in them that expand regular expression systems and matching
# ˆ Matches the beginning of the line.
# $ Matches the end of the line.
# . Matches any character (a wildcard).
# \s Matches a whitespace character.
# \S Matches a non-whitespace character (opposite of \s).
# * Applies to the immediately preceding character(s) and indicates to match zero or more times.
# *? Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.
# + Applies to the immediately preceding character(s) and indicates to match one or more times.
# +? Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”.
# ? Applies to the immediately preceding character(s) and indicates to match zero or one time.
# ?? Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.
# [aeiou] Matches a single character as long as that character is in the specified set. In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
# [a-z0-9] You can specify ranges of characters using the minus sign. This example is a single character that must be a lowercase letter or a digit.
# [ˆA-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.
# ( ) When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().
# \b Matches the empty string, but only at the start or end of a word.
# \B Matches the empty string, but not at the start or end of a word.
# \d Matches any decimal digit; equivalent to the set [0-9].
# \D Matches any non-digit character; equivalent to the set [ˆ0-9].

####################################################################################################################################################################
# End Of Chapter 11
####################################################################################################################################################################

