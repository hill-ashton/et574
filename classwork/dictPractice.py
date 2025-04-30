NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47}

#A
print((NY['QS']))
print(NY.get("QS"))
print()

#B
print(NY.get("LI", "Not in"))
print(NY.get('SI', 'absent'))
print(NY.setdefault('SI', 0.48))
print()

#C
print("LI" in NY)
print('MN' not in NY)
print()

#D
print(len(NY), min(NY), max(NY))
print(len(NY.items()),
max(NY.keys()), min(NY.values()))
print()