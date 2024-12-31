# Map and Filter

lis = ["1", "4", "7", "3"]

a = list(map(int, lis))
print(a[0] + 1)
print()

# map command is used when you want to have a particular operation over all values of an item

# map function takes two arguements 1. operation 2. list, set, tupple and etc

# converting map again into list is compulsory if you want a list output

def greater(num):
	return int(num) > 5
	
b = list(filter(greater, lis))
print(b)

# filter command gives all the value those Boolean value comes true

# It takes two arguements 1. function name 2. list