#ashton hill
#lab11_4

stuInfo1 = {
    "name":"Sergio",
    "gpa":4.0
}
stuInfo2 = {
    "name":"Jhon",
    "gpa":3.5
}
stuInfo3 = {
    "name":"Alex",
    "gpa":3.1
}

stuClass = [stuInfo1,stuInfo2,stuInfo3]
print(f"All students in the list:\n{stuClass}\n")

print("All students information:")
a = 1
for i in stuClass:
    print(f"student {a} {i}")
    a+=1
print()

print("All gpa information:")
for i in stuClass:
    print(i.get("gpa"),end="|")
print("\n")

stuInfo4 = {
    "name":"Ernie",
    "gpa":3.7
}

stuClass.append(stuInfo4)

print("All the updated information:")
for i in stuClass:
    print(f"{i.get("name")}\t\t{i.get("gpa")}")