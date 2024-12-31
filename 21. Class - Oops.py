# Class - Object Oriented Programming

class Students :
	pass

# This will make a class named students

# Starting class name with first letter capital is recommended

harsh = Students()

# We can give any variable a class by this way

# Use of parentheses is must to specify it as a function

harsh.std = 11

# By writing .templateobject we can derive it some value

print(harsh.std)
print()


# -------------- 2nd Part -----------------

class Employee :
	no_of_leaves = 7
	
ankit = Employee()

print(ankit.no_of_leaves)

# Any variable given to the class also becames for it's objects but we can only access them untill we define the same for that object

ankit.no_of_leaves = 9

print(Employee.no_of_leaves)
print(ankit.no_of_leaves)

# We can also see the variables of the class by this way

# But by using an class object we will only change the value for that object

print(ankit.__dict__)
print()

# .__dict__ enables us to see all the variables of the class in the form of a dictionary


# ------------------ 3rd Part --------------------

class Programmers :
	def details(self) :
		return f"Name is {self.name}"
		
harry = Programmers()
harry.name = "Harry"

print( harry.details() )
print()

# Here it automatically takes self inside also when we doesn't have given the self arguement

# Here the self in the details function's arguement takes itself means it takes name from name.fuction()

# Writing harry.details() automatically gives the arguement harry inside details function


# ---------------------- 4th Part -----------------------

class Constructor :
	def __init__(self, Name) :
		self.name = Name

truck = Constructor("TATA")

print(truck.name)
print()

# __init__() works as a arguement taker for main class

# If we me make some function for doing so, then we would have to run that fuction seperately as truck.functionname()


# ---------------------- 5th Part ----------------------

class Changer :
	name = "Changer"
	
	@classmethod
	def change(self, Name):
		self.name = Name
		return self.name

amit = Changer()
amit.change("Amit")

print(Changer.name)
print()

# classmethod decorator is used when we need to take whole class as the first arguement

# Here in place of self it takes the class (Changer) not the object amit and thus, chenges the class value


# ------------------- 6th Part ------------------

class Functions :
	
	@staticmethod
	def printer() :
		print("Hi I am printer function")
		
priyanshu = Functions()
priyanshu.printer()
print()

# staticmethod decorator is used when we doesn't want any self arguement inside

# This enables to use a function for only a object of specific class and not accessible by others


# ------------------ Forcing Functions --------------------

from abc import ABC, abstractmethod

class Shapes (ABC) :
	
	@abstractmethod
	def no_of_sides(self) :
		return 0
		
# This class will force every class which inherit it to make the function which is given under abstractmethod decorator, here it is no_of_sides

# So it becames compulsary to all class which inherit this class to make no_of_sides()
		

class Rectangle (Shapes) :
	def no_of_sides(self):
		pass

harsh = Rectangle()

# Here is the example for force no_of_side()

# But any object can't be made up from abstract class means from Shape()


# --------------------------- 7th Part ---------------------------

class Var :
	value = 0
	
	@property
	def printer(self) :
		return self.value
		
harsh = Var()
print(harsh.printer)

# The property decorator enables us to use a function inside the class without using ()

# Now, it can't be called using the parentheses