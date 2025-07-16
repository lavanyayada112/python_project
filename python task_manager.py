# Student Marks Manager
# A simple CLI project to manage student records
# Created by: Your Name

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)
    students[name] = marks
    print(f"{name}'s data added successfully!\n")

def view_students():
    if not students:
        print("No student data available.\n")
        return
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        print("----------------------------")
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Average: {average:.2f}")
    print("----------------------------\n")

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        marks = students[name]
        average = sum(marks) / len(marks)
        print("----------------------------")
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Average: {average:.2f}")
        print("----------------------------\n")
    else:
        print("Student not found!\n")

def menu():
    while True:
        print("==== Student Marks Manager ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Thank you for using Student Marks Manager!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()
