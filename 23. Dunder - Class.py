# Dunder Methods - Operator Overloading


# Functions starting and ending with __ are called as Dunder functions 

class Dunder :
	salary = 307
	
	def __add__(self, other) :
		return self.salary + other.salary
		
harsh = Dunder()
amit = Dunder()

print(harsh + amit)

# Here __add__() is a Dunder method and it replaces the addition sign

# This function works when we add two objects of the class


""" Similarly

We have some more Dunder Methods

1. __truediv__()
replaces the / sign


2. __str__()
replaces the object path from print(object)

ex - print(harsh) : this would print what you have in str


3. __repr__()
works same as __str__() but only in absence of it

use of repr(object) will force repr


"""