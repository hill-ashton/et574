#lab12_3mod
#ashton hill

def makePresidentFile():
    presidents = ["George Washington", "John Adams", "Thomas Jefferson"]
    with open("Presidents.txt",'w') as txt:
        for president in presidents:
            txt.write(president + '\n')

def appendPresidentFile(presidents):
    with open("Presidents.txt",'a') as txt:
        for president in presidents:
            txt.write(president + '\n')

def displayFile():
    with open("/workspaces/et574/Presidents.txt") as txt:
        for line in txt:
            print(line.rstrip())

