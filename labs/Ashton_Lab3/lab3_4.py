#lab3_4
#Ashton Hill

#A
#phoneNum is stored as an int, not a string, so it cannot be concatenated with strings.
phoneNum = "718-710-4756"
print("QCC phone number is " + phoneNum + '.')

#B
#finally is a reserved python word, and cannot be used as a variable name
fin = "happily ever after."
print("They lived " + fin)

#C
#age is an int, which cannot be concatenatred with strings, unless we cast to string. 
age = 20
print("I am " + str(age) + " years old.")

#D
#age is saved as a string, when it should be an int so it may be added by 1. Also we can cast the sum to Str to concatenate.
age = int(input("Enter your age: "))
print("Next year you will be " + str(age+1))