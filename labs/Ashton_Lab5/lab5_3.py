#lab5_3
#Ashton Hill
fours = [x*4 for x in range(0,11)]
print(fours)

twos = []
for i in fours:
    twos.append(i//2)
print(twos)

ones = twos[:]
for i in range(11):
    ones[i] = ones[i]//2
print(ones)