#ashton hill
#lab11_1
stuInfo = {
    "name" : "John Smith",
    "gpa" : 3.456,
    "age" : 20
}

for k, v in stuInfo.items():
    print(f"{k.upper()}\t{v}")
print()

stuInfo.update({"gpa":4.0})

for k in stuInfo.keys():
    print(f"{k.upper()}\t{stuInfo[k]}")
print()

stuInfo.update({"major":"CSIS"})

for v in stuInfo.values():
    print(f"{v}",end='|')
print("\n")

stuInfo.pop("gpa")
del stuInfo["age"]

print(stuInfo)

