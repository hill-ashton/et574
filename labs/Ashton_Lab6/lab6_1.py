#lab6_1
#Ashton Hill
age = int(input("Please enter your age: "))
if (age<0):
    print("invalid age.")
elif (age<2):
    print("You're a baby.")
elif (age<4):
    print("You're a toddler.")
elif (age<13):
    print("You're a kid.")
elif (age<20):
    print("You're a teenager.")
elif (age<65):
    print("You're an adult.")
else:
    print("You're an elder.")