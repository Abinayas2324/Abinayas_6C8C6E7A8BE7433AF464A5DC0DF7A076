class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.9),
]

students2 = [
    Student("David", "D004", 3.2),
    Student("Eva", "E005", 3.7),
    Student("Frank", "F006", 3.6),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

# Print the sorted student lists
print("Sorted Students 1:")
for student in sorted_students1:
    print(f"{student.name} ({student.roll_number}): CGPA = {student.cgpa}")

print("\nSorted Students 2:")
for student in sorted_students2:
    print(f"{student.name} ({student.roll_number}): CGPA = {student.cgpa}")
