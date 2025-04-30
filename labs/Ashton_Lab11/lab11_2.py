#ashton hill
#lab11_2
rank = {
    1:"Freshman",
    2:"Sophomore",
    3:"Junior",
    4:"Senior"
}
year = int(input("Enter the # of years in the school (1-4): "))
for i in rank.keys():
    if (year<1 or year>4):
        print("Invalid years.")
        break
    elif year==i:
        print(f"Year {i} = {rank[i]}")
        break

        