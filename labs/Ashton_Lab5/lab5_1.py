#lab5_1
#Ashton Hill

#A
odd_num = []
for i in range(1,10,2):
    odd_num.append(i) 
print(odd_num)

#B
num = [1,8,27,64,125,216,343,512,729,1000]
for i in num:
    print(f"{i}")

#C
cubes = [item ** 3 for item in range (1,11)]
for i in cubes:
    print(i, end = '|')
print("\n")



