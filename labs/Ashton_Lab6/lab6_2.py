#lab6_2
#Ashton Hill
users = ["admin","ash","jeff","sun","bob"]
if users:
    for i in users:
        if i=="admin":
            print(f"Hello {i.capitalize()}, would you like to see a status report?")
        else:
            print(f"Hello {i.capitalize()}, thank you for logging in again!")
else:
    print("We need to find some users.")