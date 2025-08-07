import datetime
import matplotlib.pyplot as plt
from application.services import StudentService
from domain.models import Student

class StudentMenu:
    def __init__(self, service: StudentService):
        self._service = service
    
    def run(self):
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. List All Students")
            print("3. Filter Students Older Than 22")
            print("4. Filter High GPA Young Students")
            print("5. Save Data to File")
            print("6. Show GPA Chart")
            print("7. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self._add_student()
            elif choice == "2":
                self._list_students()
            elif choice == "3":
                self._filter_older_students()
            elif choice == "4":
                self._filter_high_gpa_young_students()
            elif choice == "5":
                self._save_data()
            elif choice == "6":
                self._show_gpa_chart()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _add_student(self):
        print("\nAdd New Student")
        firstname = input("First name: ")
        middlename = input("Middle name: ")
        lastname = input("Last name: ")
        
        print("Birthday:")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        birthday = datetime.date(year, month, day)
        
        address = input("Address: ")
        phone = input("Phone: ")
        regno = input("Registration Number: ")
        gpa = float(input("GPA (0-10): "))
        
        student = Student(firstname, middlename, lastname, birthday, 
                         address, phone, regno, gpa)
        self._service.add_student(student)
        print("Student added successfully!")
    
    def _list_students(self):
        students = self._service.get_all_students()
        print("\nList of Students:")
        for student in students:
            print(student)
    
    def _filter_older_students(self):
        students = self._service.get_students_older_than(22)
        print("\nStudents Older Than 22:")
        for student in students:
            print(student)
    
    def _filter_high_gpa_young_students(self):
        students = self._service.get_high_gpa_young_students()
        print("\nHigh GPA Young Students (GPA 8-10, Age <22):")
        for student in students:
            print(student)
    
    def _save_data(self):
        filename = input("Enter filename to save: ")
        self._service.save_data(filename)
        print(f"Data saved to {filename}")
    
    def _show_gpa_chart(self):
        students = self._service.get_all_students()
        if not students:
            print("No students to display")
            return
        
        names = [s.get_fullname() for s in students]
        gpas = [s.gpa for s in students]
        
        plt.figure(figsize=(10, 5))
        plt.bar(names, gpas)
        plt.xlabel("Student Name")
        plt.ylabel("GPA")
        plt.title("Student GPA Chart")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()