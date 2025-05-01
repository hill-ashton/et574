#ashton hill
#lab11_5

def createUser(**profile):
    return profile 

def printUser(user):
    for i in user.keys():
        print(f"{i}: {user[i]}")

printUser(createUser(name = "John", age = 43, job = "Programmer", hobby = "Biking"))
print()
printUser(createUser(name = "Sara", age = 24, school = "QCC", major = "CSIS"))
