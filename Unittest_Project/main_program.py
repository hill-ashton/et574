# Updated main_program.  
def main():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                break
            else:
                print("Number of students must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    total_sum = 0
    grades = []
    for i in range(num_students):
        while True:
            try:
                grade = float(input(f"Enter grade for student {i+1} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    total_sum += grade
                    break
                else:
                    print("Grade must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 100.")
    
    # Calculate average
    average = total_sum / num_students

    # Find highest and lowest grades
    highest_grade = max(grades)
    lowest_grade = min(grades)

    # Calculate pass/fail count
    pass_count = sum(1 for grade in grades if grade >= 60)
    fail_count = len(grades) - pass_count

    print(f"The class average is: {average:.2f}")
    print(f"Highest grade: {highest_grade}")
    print(f"Lowest grade: {lowest_grade}")
    print(f"Number of students passed: {pass_count}")
    print(f"Number of students failed: {fail_count}")
    


main()
