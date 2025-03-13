#lab4_2
#Ashton Hill
grades = []
grades.append(48)
grades.append(95)
grades.append(97)
grades.append(59)
grades.append(86)
print("Current List:",grades)
total = grades[0] + grades[1] + grades[2] + grades[3] + grades[4]
print(f"Average: {(total/(len(grades))):.2f}\n")
grades.pop(0)
grades.remove(59)
print("Updated List:",grades)
print(f"Updated Average: {((grades[0]+grades[1]+grades[2])/len(grades)):.3f}")

