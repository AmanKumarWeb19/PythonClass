'''
Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
Your program should use time module to get the current hour. 
Here is a sample program and documentation link for you:

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
'''
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

import time

timestamp=time.strftime("%H:%M:%S")

if(timestamp<"12"):
    print("Good Moring")
elif(timestamp>"12" and timestamp<"17"):
    print("Good Afternoon")
elif(timestamp>"17" and timestamp<"20"):
    print("Good Evening")
else:
    print("Good Night")