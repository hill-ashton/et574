#lab12_1
#ashton hill

def displayFileLoop(path):
    with open(path) as txt:
        for line in txt:
            print(line.rstrip())

def displayFileList(path):
    with open(path) as txt:
        lines = txt.readlines()
    for line in lines:
        print(line.rstrip())


path = '/workspaces/et574/labs/Ashton_Lab12/Presidents.txt'
displayFileLoop(path)
displayFileList(path)