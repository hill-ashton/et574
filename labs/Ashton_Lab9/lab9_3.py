#lab9_3
#ashton hill
def nameFormat(first,last,middle = None):
    #None allows middle to be "False" by default
    if middle:
        print(f"{last.title()}, {first.title()} {middle[0].title()}.")
    else:
        print(f"{last.title()}, {first.title()}")
    
def main():
    nameFormat(last = "bond",first = "james")
    nameFormat(last = "henry",first = "indiana",middle = "jones")

main()