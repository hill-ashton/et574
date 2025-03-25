#lab7_1
#Ashton Hill
try:
    i = int(input("Enter an integer number, and i'll tell you if its a multiple of ten: "))
    if(i%10==0):
        print(f"{i} is a multiple of ten.")
    else:
        print(f"{i} is not a multiple of ten.")
except(ValueError):
    print("Invalid input.")