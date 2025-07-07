# List

var = [ "Harsh", "Ankit", "Amit", "Priyansu" ]
print(var)
print()

# List is written in [ ]
# All the values inside the list are taken as integer

""" List Slicing """

print(var[2])
print(var[2:4])
print(var[1:4:2])
print()

# Works same as string

# Works with negative too but not recommended to take more than -1 because sometimes it throws error

var[2] = "Anubhav"
print(var)
print()

# Replaces the desired value from given


""" Functions """

print(len(var))
print()

# Prints length

# We also have

# min() lowest number, First word
# max() highest number, Last word

var.sort()
print(var)

# Sort fuction sorts the list in ascending

# In the case of list you have to first use function then print

#Similarly, we have 

var.reverse()
print(var)
 
# This will reverse the order of list

var.append("Prakhar")
print(var)

# Append means add at the last

var. insert(3, "Sahil")
print(var)

# Inserts the value at desired position
# Take two arguments: 1. Position, 2. Value

var.remove("Harsh")
print(var)
print()

# Removes the given value from the list

a = ", ".join(var)
print(a)

# .join function joints the items in the list with the arguement given before


""" Comprehension """

ls = [ i for i in range(20) if i%3 == 0 ]
 print(ls)

# we could also make a list by using this method

# First arguement takes the variable name

# Second - position of variable

# Third - condition

# We could also give 1, 2 arguements only