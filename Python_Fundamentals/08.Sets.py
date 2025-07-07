# Sets

s = set ( )

# Set ( ) stores set of numbers inside
# Same set as we studied in class 11

l = [1, 2, 3, 4]
print ( set( l ) )

# A list is stored inside a set
# But set only keeps unique values

"""

  List Qualities

This also has all list Qualities like :
    
    len
    min
    max
    type

"""


""" Functions """

s.add(1)
s.add(2) 
print(s)

# Works same as append

s.remove(2)
print (s)

# Works same as remove in the list

s1 = s.union( { 1, 2, 3 } )
print (s1)

# Works same as union in maths

s2 = s.intersection({ 1, 2, 3 })
print(s2)

# Works same as intersection


""" Comprehension """

items = {item for item in range(3)}
print(items)

# Set builder

# First arguement takes the variable

# Second arguement takes the definition of variable