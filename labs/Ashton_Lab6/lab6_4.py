vehicles = ["car","Truck","boat","PLANE"]
let = (input("Enter a search letter: "))
if len(let)==1:
    for i in vehicles:
        temp = True
        for j in i:
            if let.capitalize()==j.capitalize():
                print(f"{i} contains {let} and its in position {vehicles.index(i)}")
                temp = False
        if(temp):
            print(f"{i} does not contain {let}.")
else:
    print("Invalid search letter.")