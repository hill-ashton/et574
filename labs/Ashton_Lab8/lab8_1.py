#lab8_1
#Ashton Hill
from math import fmod, floor

while True:
    try:
        n1 = eval(input("Enter a numerator: "))
        n2 = eval(input("Enter a denominator: "))
        if n2!=0:
            print(f"{n1} mod {n2} = {floor(fmod(n1,n2))}")
            break
        else:
            print("Error: Denominator cannot be zero. Try again.")
    except:
        print("Exception: Invalid input data type. Please re-enter.")
    