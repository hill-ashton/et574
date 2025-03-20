#lab6_5
#Ashton Hill

#A
#In order to properly compare n and 7, you need to use == to evaluate.
#To find the square root(raise to power of 2) you must use double asterisks **
n = eval(input("Enter a number: "))
if n == 7:
    print("The square of", n,"=",n**2)

#B
#when adding the second argument using our 'and' logic operator, we must specify n again when comparing it to another value
n = 9
if n>5 and n<9:
    print("Yes")
else:
    print("No")

#C
#if statement must finish with colon
#must explicitly compare "Computer Technology" to variable major, or else it will always be true.
major = "Computer Science"
if major == "Engineering Technology" or major == "Computer Technology":
    print("CS in the Category")

#D
#must compare variables with == to check if they are identical. 
a,b = 1, 1.0
if a==b:print("same")