# DataTypes

print(type("Hello World"))
print()

# Type function give the type of the data stored

var1 = "41"
var2 = "57"

print(var1 + var2)

# Addition of two strings concatinate them

print(int(var1) + int(var2))

# Int() function can change any data type into integer if possible

"""
Similarly, we have :

str()
float()

"""

# we could also multiply the number in int statement

print(2 * int(var1) + int(var2))



# Strings

mystr = "Hello World"

print (len(mystr))
print()

# len() gives the length of the string (no. of characters)


""" String Slicing """

print(mystr[0])

# If we want a particular character of the string we can write the place of character in a big bracket after string name

# In programming number starts from 0

print(mystr[0:5])

# This is used when we want a particular part to the string by using : between the start and end character

# The upper valuse in included but lower value in excluded

print(mystr[0:11:2])

# The the second : represents the no of characters to be skipped

# 2 means it only shows every second character after the previous one


""" Blanks """

print(mystr[8:])

# Leaving any space blank will take the extreme position of it

# Example

print(mystr[ :11])

# Blank was taken as 0

print(mystr[ : : ])

# Leaving second : blank will take is as 1


""" Negatives """

print(mystr[-8:-1])

# - reprents the counting from the last

# -0 doesn't exist so the number here satrt from -1

print(mystr[ : : -1])
print()
# Taking the number after second : in negative will reverse the string


""" Functions """

print(mystr.isnumeric())
print()

# .isnumeric() tells us whether the string is numeric or not 

# Is is a Boolean datatype so, it answers only in true and false

"""
Similarly, we have

.isalpha()
# Check about alphanumeric

.endswith()
# Check where it ends with given characters

.count()
# Count the number of characters

.capitalize()
# Capitalise the first letter

.find()
# Find the position of the characters

.lower()
# Decapitalise the whole string

.upper()
# Capitalise the whole string

.replace("" , "")
# Take two arguments 1. to replace 2. with what 

"""

params = mystr.split(" ")
print(params)
print()

# .split() takes one arguement and splits the string into different part according to arguements and make a list out of it


""" F strings """

a = "Harsh"
print("This is %s" %a)

# %s represents the place where we want to add variable

# After the string %variable inserts the value

# This is suitable for few variables but not for a huge amount

print(f"This is {a}")
print()

# Writting f before string makes it f string

# Use of { } inside the f string to specify the variables in the space

# We could also give any operation inside f string


""" Raw String """

print(r"\n This is a raw string")

# raw string is made using r before " " 

# raw string behave like a string without any escape sequence character and variable names