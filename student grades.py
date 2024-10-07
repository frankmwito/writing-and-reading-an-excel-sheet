# excel spread sheet of students grades

from openpyxl import Workbook

# Create a new workbook and select the active worksheet
workbook = Workbook()
worksheet = workbook.active

# Get the number of students and handle the case where the input is not a valid integer
try:
    num_of_students = int(input("Enter the number of students: "))
except ValueError as ve:
    print("Invalid input: please enter a valid number.")
    exit()  # Exit if the input is invalid

# Initialize a list to store student names and grades
student_grades = [["Names", "Grades"]]  # Should be a list, not a tuple

# Get student names and grades, handling invalid input types (e.g., non-float grades)
try:
    for i in range(num_of_students):
        names = input(f"Enter the name of student @{i+1}: ")
        grades = float(input(f"Enter the grade of student @{i+1}: "))
        student_grades.append([names, grades])
except ValueError as ve:
    print("Invalid input: Please enter valid numbers for grades.")

# Always write the data to the Excel file, even if there's an exception
finally:
    for data in student_grades:
        worksheet.append(data)
    
    workbook.save("students_grades.xlsx")
    print("Excel file 'students_grades.xlsx' created successfully!")

    


