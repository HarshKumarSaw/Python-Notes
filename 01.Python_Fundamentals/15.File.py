# Files


""" Open And Read """

f = open("Test.txt")

# open() command is used to open a file

# We have to store it in some variable so that we could read or write in it.

r = f.read()
print(r)

# read() function is used to read the content of the file

# This function will only read the file, we have to print it seperately

f.close()

# close() function closes the file we have opened earlier

# It's always a good practice to close the file

print()

with open("Test.txt") as f :
	
	a = f.read()
	print(a)
	
# By this way you don't need to close the file
# Works same as above described

print()

"""
Modes to open the file

r - read mode (default)
w - write mode
a - append mode
r+ - read and write both

t - text mode (default)
b - binary mode

we could take the fusion of both set of codes

"""

# open() takes two arguements 1. path 2. mode

f = open("Test.txt", "rb")
r = f.read(6)
print(r)

# This prints the binary form of the file

# read function takes the no. of character to be printed

r = f.read(6)
print(r)
print()

# The number everytime starts from where it was ended for every read() function

e = f.readline()
print(e)

# readline() function reads only a single line

g = f.readlines()
print(g)

# readlines() function reads all the lines 

f.close()


""" Writing a file """

f = open ("Test2.txt", "w")

# This will open up the file if existing or will create a new file

f.write("Ye hum file ko rewrite kar rahe hai")

# This will clear all the data of file and write the following data

f.close()


""" Appending A File """

f = open ("Test2.txt", "a")
f.write("\nMaje ma.")
f.close()

# This will append the content in the file

# We could also use r+ mode to read and write both at the same time

print()


""" File slicing """

f = open ("Test.txt")
print(f.tell())

print(f.readline())
print(f.tell())

# tell function tells where our pointer actually is

f.seek(0)
print(f.readline())

# seek function locates the pointer at desired position

f.close()