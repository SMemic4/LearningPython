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
# When searching through data in a file, it is a very common pattern to read through a file, ignoring most of the lines and only processsing lines which meet a particular condition
# A combination of the pattern for reading a file with string methods allow for the creation of simple search mechnanisms
# For example, if one wanted to read a file and only print out lines which started with the prefix "From:" the string method startswith could be used to select those desired lines

fhand = open('mbox-short.txt')

for line in fhand:
    if line.startswith("From:"):
        print(line)
        
# The output does what it's supposed to but there are extra blank lines that appear in the prompt. This is due to the invisible newline character
# Each line ends with a newline, so the print statementthe string in the variable line, which includes a newline and then print adds another newline resulting in the double spacing effect
# Line slicing could be used to print all but the last character, but a simpler approach would be striping the whitespaces from the from the rightside of the string

fhand = open("mbox-short.txt")

for lines in fhand:
    if lines.startswith("From:"):
        print(lines.strip())
        
# When the program runs the output is the same but without the extra blank lines
# As file processing programs become more complicated, structure the search loops using continue. 
# This will tell the program to look for interesting programs and to skip uninteresting lines

fhand = open("mbox-short.txt")

for lines in fhand:
    if not lines.startswith("From:"):
        continue
    print(lines.strip())
    
# The output of the program is the same, but processing only occurs for lines where the line fulfills the condition

# The find string method can be used to simulate a text editor that finds lines where the search string occurs anywhere in the line
# Since find looks for an occurrence of a string within another string and either returns the position of the string or -1 if the string was found, the following loop works to find specific emails

fhand = open("mbox-short.txt")

for lines in fhand:
    if lines.find("@uct.ac.za") == -1:
        continue
    print(lines.strip())
    
# Here the contracted form of the if statement is used where a continue is on the same line as the if
# The contracted form of the if functions the same as if the continue were on the next line indented

####################################################################################################################################################################
# 7.6 Letting the user choose the file name
####################################################################################################################################################################
# It is not feasible to edit the python code every time it needs to process a different file
# It would be more usable to ask a user to enter the file name string each time the program runs si they can use the program on different files without changing the python code

fname = input("Enter file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)

# However this code lacks the ability to handle if the user enters the name of a file that does not exist

####################################################################################################################################################################
# 7.7 Using try, except, and open
####################################################################################################################################################################
# The above code will fail to run if the user enters in a nonexistent file name. This can be circumvented using try except and open

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)

# The exit function terminates the program. It is a function that is called that never returns 

# Protecting the open call is a good example of the proper use of try and except in a python program

####################################################################################################################################################################
# 7.8 Writing Files
####################################################################################################################################################################
# To write a file, it must be opened with mode "w" as a second parameter

fout = open("output.txt", "w")
print(fout)

# If the file already exists, opening it in write mode clears out the old data and starts fresh, so proceed with caution. If the file doesn't exist, a new one is created
# The write method of the file handle object puts data into the file returning the number of characters written. The default write mode is text for writing (and reading) strings

line1 = "THis here's the first line of this text \n"
fout.write(line1)

# Again. the file object keeps track of where it so, so calling write again will add new data to the end
# The end of the line must be managed by explicity inserting the newline character when ending a line
# The print statement automatically appends a newline, but the write method does not add the new line automatically

line2 = 'the emblem of our land.\n'
fout.write(line2)

# When one is done with writing the file, the file must be closed so the last bit of data is physically written to the disk so it will not be lost if the power goes off

fout.close()

# Pythong automatically closes the files when the program closes, but when writing files it is important to explicitly close the files so as to leave nothing to chance

####################################################################################################################################################################
# 7.11 Exercises
####################################################################################################################################################################
# 1. Write a program to read through a file and print the contents of the file (line by line) all in upper case. 

fname = input("Enter the name of the file: ")
try:
    fhand = open(fname)
except:
    print("Not a legit file")
for lines in fhand:
    print(lines.upper())
    
# 2, Write a program to prompt for a file name and then reads for lines that start with "X-DSPAM-Confidence: 0.8475", extract the floating-point number count the lines and compute the average spam confidence

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("File not found")
    quit()

count = 0
total = 0

for lines in fhand:
    if fname.startswith("X-DSPAM-Confidence: "):
        start = lines.find(" ")
        word2 = lines[start+1:]
        word2 = word2.strip()
        word2 = float(word2)
        total = total + word2
        count = count + 1

avg = total / count
print("Average spam confidence:", avg)

####################################################################################################################################################################
# End of Chapter 7
####################################################################################################################################################################
















