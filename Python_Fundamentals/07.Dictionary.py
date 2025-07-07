# Dictionary

d1 = {"Harsh" : "Biology", "Ankit" : "Maths"}
print(d1)
print()

# Dictionary is written between {}
# Dictionary stores two arguments

d2 = {"Amit" : { "Biology" : "Neet", "Maths" : "Jee" }}
print(d2)
print()

# Dictionary could also have dictionaries inside

print(d1["Harsh"])
print(d2["Amit"] ["Biology"])
print()

# Dictionary slicing same as string slicing

d2 ["Prakhar"] = "Neet"
print(d2)
print()

# Works same as append

del d2 ["Amit"]
print(d2)
print()

# Works same as remove

d3 = d2

# This will not make a new dic of d3 but points towards the same

d3 = d2.copy

# Makes the copy of d2 inside d3


""" Functions """

print(d1.get("Harsh"))
print()

# Print the value of key

d1.update({ "Priyanshu" : "Neet" })
print(d1)
print()

# Same as append

print(d1.keys())

# Prints all the keys

print(d1.items())
print()

# Prints all the items and keys

di1 = { value : key for key, value in d1.items() }
print(di1)

# Reverse the value

list1 = [ [13, 24], [28, 82], [61, 34] ]

dict1 = dict (list1)
print(dict1)
print()

# dict command is used to typecast list, set or tupple into dictionary


""" Comprehension """

My_dic = { i : f"k{i}" for i in range (10) if i%3 == 0}
print(My_dic)

# Short dictionary

# First arguement takes the key : item

# Second arguement takes the source of item

# Third arguement takes the condition

# We can also use only 2 arguements and not 3