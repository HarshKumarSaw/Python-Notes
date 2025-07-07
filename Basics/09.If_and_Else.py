# If Else

var1 = 86

inp = int(input())
print()

if var1 > inp :
    print (inp, "is lesser than 86")
    print()
    
# if takes an statement and : which when goes true it goes inside the :

# But if statement doesn't stop after getting one argument true so, we have elif

elif var1 == inp :
    print(inp, "is equal to 86")
    print()
    
# We use == because it checks whether they are equal to each other or not

# We don't use = because this will make var1 equal to inp 
    
else :
    print (inp, "is greater than 86")
    print()
    
# else : works when if statement gets false

list1 = [1, 2, 3, 6]
print(list1)

if 2 in list1 :
    print ("Yes we have 2 in list")
    print()
   
# in checks whether it have it inside or not

if 5 not in list1 :
    print("No we doesn't have 5 in list")

print()
    
# not in checks the non existence of it

# We have use if instead of elif because after getting the first statement true the elif function doesn't works

if var1 < inp : print ("Bigger")

# One liner if statement

print("Bigger") if var1 < inp else print ("Smaller")

# Short hand if and else