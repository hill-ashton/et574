#Lab7_6
#Ashton Hill
n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))

if(n1<n2):
    while n1<=n2:
        print(f"{n1}",end = '|')
        n1+=1
if(n1>n2):
    for i in range(n1,n2-1,-1):
        print(f"{i}",end = '|')
else:
    print("n1 = n2")