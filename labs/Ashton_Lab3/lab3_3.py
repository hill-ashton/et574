#lab3_3.py
#Ashton Hill
try:
    
    int1 = int(input("Please enter the first integer: "))
    int2 = int(input("Please enter the second integer: "))
    int3 = int(input("Please enter the third integer: "))

    min = min(int1,int2,int3)
    max = max(int1,int2,int3)
    mid = (int1+int2+int3)-min-max

    print("Before sorting:",int1,int2,int3,sep=' ')
    print("After sorting:",min,mid,max,sep=' ')

except ValueError:
    print("Exceptions: Invalid Input")
