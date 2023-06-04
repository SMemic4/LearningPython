####################################################################################################################################################################
# Chapter 7: Files
####################################################################################################################################################################
# 7.1 Persistence
####################################################################################################################################################################
# The central processing unit (CPU) is used during conditional execution, functions, and iterations
# Data structures are created and used in the main memory. 
# The CPU and memory are where the software works and run. It is where all the "thinking" occurs
# When a computer is powered off anything stored in the CPU or main memory is erased
# Secondary memory (or files) are not erased when the power is turned off. 


####################################################################################################################################################################
# 7.2 Opening Files
####################################################################################################################################################################
# To read or write a file (on a hard drive), the first thing is the file must be opened
# Opening the file communicates with the operating system which knows where the data for each file is stored
# To open the mbox.txt file in the following good, the file should be stored in the same folder in which pyhton is started

fhand = open("mbox.txt")
print(fhand) # <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>

# If the open is successful, the operating system returns a file handle. The file handle is not the actual data contained in the file. but instead is a "handle" that can be used to read the data
# A handle is given if the requested file exists and the proper premissions to read the file

# If the file does not exsit, open will fail with a traceback, and the handle to access the contents of the file will not be provided 

fhand = open('stuff.txt') # Traceback (most recent call last): FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'

# Try and except can be used to deal with these situations more gracefully for attempts at opening a file does not exist

####################################################################################################################################################################
# 7.3 Text files and lines
####################################################################################################################################################################
# A text file can be thought of as a sequence of lines, much like a python string can be thought of as a sequence of characters
# "mbox.txt" are the standard format for a file containing multiple mail messages. 
# The lines which start with "From" seperate the messages and the lines which start with "From" are part of the messages
# To break the file into lines, there is a special character that represents the "end of the line" is called the newline character

# In python, the newline character is represented as a backslash-n in string constants. Even though this looks like two characters, it is actually a singe character
# When using \n in the interpreter it shows up in the string but when it is printed as a string, the string is broken up into new lines by the newline character

stuff = "Hello\nMarsey!"
stuff # 'Hello\nMarsey!'
print(stuff)
# Hello
# Marsey!

stuff = "X\nY"
len(stuff) # 3

# The length of the string X\nY is three character because the newline character is a single character
# When looking at the lines in a file, imagine that there is a special invisible character called the newline at the end of each line that marks the end of the line
# So the newline charcter separates the characters in the file into lines

####################################################################################################################################################################
# 7.4 Reading Files
####################################################################################################################################################################
# While the file handle does not contain the data for the file it is quite easy to construct a for loop to read through and count each of hte lines in a file"

 fhand = open('mbox.txt') #
count = 0
for line in fhand:
    count = count + 1
print("Line count:", count) # Line count:  132045

# The file handle can be used to sequence in the for loop
# The for loop simply counts the number of lines in the file and prints them out
# The rough translation is: "for each line in the file represented by the file handle, add one to the count variable"

# The reason that the open function does not read the enttire fil is that the file might be quite large with many gigabytes of data.
# The open statement takes the same amount of time regardless of the size of the fille
# The for loop actually causes the data to be read from the file

# When the file is read using a for loop in this manner, Python takes care of splitting the data in the file into separate lines using the newline character
# Python reads each line through the newline and includes the newline as the last character in the line variable for each iteration of the for loop
# Because the for loop reads the data one line at a time, it can efficiently read and count the lines in very large files without running out of main memory to store the data
# THis metho d can count the lines in any size file using very little memory since each line is read, counted, and then discarded

# If the file is relatively small compared to the size of your main memory, the whole file can be read into one string using the read method on the file handle

fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp)) # 94626
print(inp[:20]) # From stephen.marquar

# In this example, the entire contents (all 94,626 characters) of the file mbox-short.txt are read directly into the variable inp. 
# The following line, slices and prints out the first 20 characters of the string data stored in inp

# When the file is read in this manner, all the characters including all of the lines and newline characters are one big string in the variable inp
# It is a good idea to store the output of read as a variable because each all to read exhausts the resource

fhand = open('mbox-short.txt')
print(len(fhand.read())) # 94626
print(len(fhand.read())) # 0

# Remeber that this form of the open function should only be used if the file data will fit comfortably in the main memory of the computer
# If the file is too large to fit in the main memory, you should write the program to read the file in chunks using a for or while loop

####################################################################################################################################################################
# 7.5 Searching through a file
####################################################################################################################################################################








