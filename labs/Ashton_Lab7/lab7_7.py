#Lab7_7
#Ashton Hill
i = 1
ls = []
sum = 0
while i != 0:
    i = float(input("Enter a nunber or 0 to stop: "))
    if i!=0: ls.append(i)
for j in ls:
    sum+=j
print(f"Sum = {sum}")
print(f"Average = {round((sum/(len(ls))),2)}")
print(f"Number(s) entered:\n{ls}")

