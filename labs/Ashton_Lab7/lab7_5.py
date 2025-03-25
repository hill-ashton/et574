#lab7_5
#Ashton Hill
import random
random.seed()
amt = int(input("Enter the number of grades in the list: "))
grades = []
passGrades = []
while len(grades)<amt:
    grades.append(random.randint(0,100))
passing = int(input("Enter the passing grade: "))
for i in grades:
    if i >= passing:
        passGrades.append(i)
print(f"Updated List: {passGrades}")
print(f"Original List: {grades}")