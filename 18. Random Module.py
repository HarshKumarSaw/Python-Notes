# Random Module

import random

# random is a built in module in python

a = random.randint(0, 100)
print(a, "\n")

# randint function generates a random integer between two given numbers

b = random.random()
print(b, "\n")

# random function generates a random number between 0 and 1

lst = ["Harsh", "Ankit", "Amit"]
c = random.choice(lst)
print(c)

# choice function gives a random item from list