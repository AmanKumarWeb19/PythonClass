# a=int(input("Enter Your Age:-"))
# print("Your age is:",a)

# if(a>18):
#     print("You can drive")
# else:
#     print("you can not drive")

# num=int(input("Enter the num:-"))

# if(num<10):
#     print("number is in single digit")
# elif(num==0):
#     print("Equal to Zero")
# elif(num==999):
#     print("Number is Special")
# else:
#     print("Number is positive")

                                        # Neated If else:-


num=22
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<=10):
        print("number is between 1 to 10")
    elif(num>10 and num<20):
        print("number is between 11 to 20")
    else:
        print("Number is greater than 20")  
else:
    print("Number is Zero")      