# Try and Except

a = input()
b = input()

try :
	print ("\nSum of these two numbers is", int(a) + int(b))
	
except Exception as e :
	print(e)
	
# try command tries to execute the command written inside but if any error occurs it doesn't operate the command

# If try fails execpt works and Exception is use to take the error

else :
	print("\nCode executed")
	
# This will run only when except is not running

finally :
	print("\nYe to hona hi tha")
	
# This will run definately after try, execpt and else