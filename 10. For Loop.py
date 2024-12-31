# For Loop

list1 = ["Harsh", "Amit", "Ankit", "Priyanshu", "Prakhar"]

for item in list1 :
	
	print (item)

print()
	
# for takes 1 argument which is key in group
# for loop works till there is no data left to show

list2 = [ ["Harsh", "Neet"], ["Amit", "Jee"], ["Ankit", "Jee"], ["Prakhar", "Neet"] ]

for item in list2 :
	
	print (item)
	
print()

# if we have list of lists then it print seprate lists

for student, exam in list2 :
	
	print(student, exam)
	
print()
	
# We can manually give any names to our items using for loop and multiple using comma to seperate

dict1 = dict( list2 )
print(dict1)
print()

for item in dict1 :
	
	print(item)
	
print()
	
# We can also print the dictionary the same way

for student, exam in dict1.items() :
	
	print (student, exam)
	print()
	
# But to print multiple values we need to use .items() fuction

for item in range(3) :
	print(item)
	
print()
	
# in range starts from 0 and goes to n - 1 here 2

# It simply used when we want numbers in increasing order

for item in range(3, 6) :
	print(item)
	
print()
	
# range starts from first arguement and goes till n - 1 here 5


""" For with Else """

khana = ["roti", "sabji", "dal", "bhat"]

for item in khana :
	
	if item == "chawal" :
		break

else :
	print("item not found")
	
# else statement is only executed when for loop ends normally

# if for loop ends with the help of the break else function doesn't work