# Factorial Finder - advance for loop


# Iterative Method 

def factorial(n) :
	
	fac = 1
	
	for i in range(n) :
		fac = fac * (i + 1)
		
	return fac

# Here the value of i goes from 0 to n

# Everytime we return fac the value of fac gets updated

n = int(input("Which factorial you want : "))

print(factorial(n))
print()


# Recursive Method

def recur(n) :
		
		if n == 1 :
			return 1
			
		else :
			return n * recur(n - 1)
			
# Here, the it returns 1 when the value of v reaches 1

# v get multiplied with recur(v - 1) until it gets the value of v = 1

"""
v * recur(v - 1)
v * recur(v - 1) * recur(v - 2)

and so on, till the value of v reaches 1

v * recur(v - 1) * .................. * 1

"""						
n = int(input("Which factorial you want : "))
print(recur(n))

print()


""" Use of iterative and recursive """

# iterative is used when you have just 1 variable to play with increasing order of some set of numbers

# recursive is usefull when you have to play with the operation of one value, x with the previous value of x