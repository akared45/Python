from datetime import datetime
from domain.student import Student

def display_menu():
    print("\nStudent Management System")
    print("1. Add student")
    print("2. Display all students")
    print("3. Filter students above 22 years old")
    print("4. Filter students with GPA 80-100 and below 22 years old")
    print("5. Save students to file")
    print("6. Display GPA chart")
    print("7. Exit")

def get_student_input() -> Student:
    regno = input("Enter registration number: ")
    firstname = input("Enter first name: ")
    middlename = input("Enter middle name: ")
    lastname = input("Enter last name: ")
    while True:
        try:
            birthday = datetime.strptime(input("Enter birthday (YYYY-MM-DD): "), '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    while True:
        try:
            gpa = float(input("Enter GPA (0-100): "))
            if 0 <= gpa <= 100:
                break
            print("GPA must be between 0 and 100")
        except ValueError:
            print("Invalid GPA. Please enter a number")
    
    return Student(firstname, middlename, lastname, birthday, address, phone, regno, gpa)

def display_students(students: list[Student]):
    if not students:
        print("No students found")
        return
    for student in students:
        print(f"RegNo: {student.regno}, Name: {student.get_fullname()}, "
              f"Age: {student.get_age()}, GPA: {student.gpa}, "
              f"Address: {student.address}, Phone: {student.phone}")