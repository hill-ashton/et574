#lab5_4
#Ashton Hill
try:
    x = int(input("Enter a range: "))
    list = [i for i in range(1,x+1,1)]
    #print(list)
    y = int(input("Enter an integer number: "))
    print("Multiplication Table of ",y)
    for i in list:
        print(f"{i}\t*\t{y}\t=\t{i*y}")
except ValueError:
    print("Invalid Input.")