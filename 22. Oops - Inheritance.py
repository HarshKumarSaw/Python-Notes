# Class - Inheritance


# ----------------- Single Inheritance ------------------

class Employee :
	salary = 20000
	
class Programmer(Employee) :
	pass

harsh = Programmer()
print(harsh.salary)

# We can simply inherit the class into another just by giving it inside the parentheses

# Inheritance enables the class to use all the variables and functions of the parent class

class Bada :
	
	def __init__(self, Name, Age) :
		self.name = Name
		self.age = Age
	
	def printdetails(self) :
		return f"Name = {self.name}, Age = {self.age}"

class Inherited (Bada) :
	pass

amit = Inherited("Amit", 16)
print(amit.printdetails())
print()

# Here if we inherit a class with a constructor then we have to specify it's arguements when we initialise an object with that class


# ------------------- Multiple Inheritance -----------------------

class First :
	value = 2
	
class Second :
	value = 3
	
class Third (First, Second) :
	pass

ankit = Third()
print(ankit.value)
print()

# Here if we give multiple class to inherit then it will first looks for the first class given as arguement


# --------------- Multilevel Inheritance ---------------

class Dad :
	runs = "100m"
	jumps = "10m"
	
class Son(Dad) :
	runs = "200m"
	
class Grandson(Son) :
	pass

harsh = Grandson()

print(harsh.runs)
print(harsh.jumps)
print()

# Here Grandson class inherited both son and dad

# Grandson first goes inside son then son goes inside dad and thus the value of son overwrites the value of runs for grandson


# -------------------------- Overriding ------------------------

class A :
	var = "Inside A"
	
	def __init__(self) :
		self.var = "Inside constructor of A"
		
class B(A) :
	var = "Inside B"
	
a = B()

print(a.var)
print()

# Any variable is first tried to find in the constructor of the class then in the constructor of inherited class

# Then after inside the class - inside the inherited class - inside the functions of the class


# --------------------- super() ---------------------

class C(A) :
	
	def __init__(self) :
		self.var = "Inside C"
		super().__init__()
		
c = C()
print(c.var)

# Here the super() calls the function given to it as a .functionname

# When the constructor of A was called by the super function the value of var gets overwrite