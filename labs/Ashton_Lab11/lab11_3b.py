#ashton hill
#lab11_3b

#importing dictionary charNum from 3a
from lab11_3a import charNum

let = [chr(ord('A') + i) for i in range(26)]
num = [i*100 for i in range(1,27)]

numChar = dict(zip(num,let))

for i in numChar.keys():
    print(f"{i} {numChar[i]}",end='|')
print("\n")

all = charNum.copy()
all.update(numChar)
print(all)