#lab12_1
#ashton hill

filename = 'Presidents.txt'
with open(filename) as txt:
    lines = txt.readlines()

for line in lines:
    print(line.rstrip())