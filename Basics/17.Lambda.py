# Lambda 

# Lambda are nothing but one liner functions

def minus(x, y) :
	return x- y

minus = lambda x, y : x - y

# Both above functions works same

# Lambda is alternative for small functions 

x = int(input("Entre your first number : "))
y = int(input("Entre your second number : "))

print("\nAddition of both numbers =", minus(x, y))