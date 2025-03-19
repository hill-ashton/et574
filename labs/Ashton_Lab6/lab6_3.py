users = ["admin","jim","jeff","sun","bob"]
username = input("Enter your user name: ")
og = True
print
for i in users:
    if username==i:
        og = False
if(og):
    users.append(username)
    print(f"Great, {username} is still available.")
    print(f"Updated users: {users}")
else:
    print(f"Sorry, {username} that name is taken.")
    print(f"Current users: {users}")
        