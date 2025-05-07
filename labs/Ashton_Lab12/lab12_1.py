#lab12_1
#ashton hill

def displayFileLoop(path):
    print("Using Loop:")
    with open(path) as txt:
        for line in txt:
            print(line.rstrip())

def displayFileList(path):
    print("Using List:")
    with open(path) as txt:
        lines = txt.readlines()
    for line in lines:
        print(line.rstrip())


path = '/workspaces/et574/labs/Ashton_Lab12/Presidents.txt'
displayFileLoop(path)
print()
displayFileList(path)