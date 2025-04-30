#ashton hill
#lab11_3a
letters = [chr(ord('a') + i) for i in range(26)]
#chr() accepts an ascii numeric value(a number), returns the ascii character represented by the numeric value
#for example, chr(97) would return 'a'
#ord() does the opposite of chr(), accepts a char, returns the ascii numeric value represented by the char
#ord('a') would return 97
numbers = [i+1 for i in range(26)]

charNum = dict(zip(letters,numbers))
print()
for i in charNum.keys():
    print(f"{i} {charNum[i]}",end='|')
print("\n")