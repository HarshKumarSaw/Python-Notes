# Time Module

import time

initial_time = time.time()
print(initial_time)
print()

# time.time() returns the number of seconds from a specific time

local_time = time.asctime(time.localtime(time.time()))
print(local_time)
print()

# This is the way to get the present time in representable mannner

for i in range (3) :
	
	print("Programm stops for 2 seconds")
	time.sleep(2)
	
# time.sleep() stops the programm for certain seconds