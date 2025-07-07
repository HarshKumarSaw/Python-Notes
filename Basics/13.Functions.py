# Functions

def func1() :
	
	print("Hello Into Function World")
	print()
	
func1()

# Functions are define by def command and using parentheses after name

# Name using the parentheses can use to call the function

def func2(a, b) :
	
	print("Now we are in second stage", a+b)
	print()
	
func2(5, 7)

# We can give multiple input in fuctions by writing there names inside function name

# The values of inputs are given while calling the function, the same way as defined

print ( func2(37, 35) )
print()

# Here we get a none value because our function just do it's job not return any output

def func3(a, b) :
	
	"""This will calculate the average of two numbers"""
	
	average = (a+b) /  2
	return average

print (func3(245, 247))
print()

# return command gives the output of function

# A comment written in the first line of the function is called as doc string

print(func3.__doc__)
print()

# This statement will print the docstring of the function


""" *Args and **kwargs """

def funcarg(*args) :
	
	for item in args :
		
		print(item)
		

lst = ["Harsh", "Ankit", "Amit", "Prakhar"]

funcarg(*lst)
print()

# Args are used when you want unlimited number of arguements inside any function

# * is necessary inside function() to specify it as arg and name arg can be changed

# We can also give more arguements with args but only before arg not after

# arg arguement can also be left blanked while calling the fuction

def funckwarg(**kwargs) :
	
	for item, key in kwargs.items() :
		
		print(item, key)
		

lst = {"Harsh" : "Biology", "Ankit" : "Maths", "Amit" : "Maths" , "Prakhar" : "Biology"}

funckwarg(**lst)

# Kwargs works same as Args but it takes dictnaries and arg takes list, set, tupple

# Kwargs can be used as a arguement after Args 

# ** is ths sign to specify kwargs