#lab12_2
#ashton hill

presidents = ["George Washington", "John Adams", "Thomas Jefferson"]

def makePresidentFile1():
    with open("Presidents2.txt",'w') as txt:
        for president in presidents:
            if(president!="Thomas Jefferson"):
                txt.write(president + '\n')

def makePresidentFile2():
    with open("Presidents3.txt",'a') as txt:
        for president in presidents:
            txt.write(president + '\n')

makePresidentFile1()
makePresidentFile2()