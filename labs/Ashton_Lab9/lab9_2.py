#lab9_2
#ashton hill
def nameFormat(first,middle,last):
    print(f"{first.title()} {middle[0].title()}. {last.title()}")

def main():
    nameFormat("john","stu","smith")
    nameFormat(last = "kennedy",first = "john",middle = "fitzgerald")

main()