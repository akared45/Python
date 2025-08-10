import matplotlib.pyplot as plt
import os

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Student(Person):
    def __init__(self, id, name, gpa):
        super().__init__(id, name)
        self.gpa = gpa

    def __str__(self):
        return f"{self.id:<10} {self.name:<20} {self.gpa:<10.2f}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            student_id = input("Enter student ID: ").strip()
            if any(student.id == student_id for student in self.students):
                print("Student ID already exists!")
                return

            name = input("Enter student name: ").strip()
            if not name:
                raise ValueError("Student name cannot be empty!")

            gpa = float(input("Enter GPA (0-10): "))
            if not 0 <= gpa <= 10:
                raise ValueError("GPA must be between 0-10!")

            self.students.append(Student(student_id, name, gpa))
            print("Student added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def display_all_students(self):
        try:
            if not self.students:
                print("Student list is empty!")
                return

            print("\nAll Students:")
            print("-" * 50)
            print(f"{'ID':<10} {'Name':<20} {'GPA':<10}")
            print("-" * 50)
            for student in self.students:
                print(student)
        except Exception as e:
            print(f"Error displaying students: {e}")

    def display_excellent_students(self):
        try:
            excellent_students = [s for s in self.students if s.gpa >= 8]
            if not excellent_students:
                print("No students with GPA >= 8!")
                return

            print("\nExcellent Students (GPA >= 8):")
            print("-" * 50)
            print(f"{'ID':<10} {'Name':<20} {'GPA':<10}")
            print("-" * 50)
            for student in excellent_students:
                print(student)
        except Exception as e:
            print(f"Error displaying excellent students: {e}")

    def save_to_file(self):
        try:
            with open('students.txt', 'w', encoding='utf-8') as f:
                for student in self.students:
                    f.write(f"{student.id},{student.name},{student.gpa}\n")
            print("Student list saved to file successfully!")
        except IOError as e:
            print(f"File save error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def view_student_by_id(self):
        try:
            student_id = input("Enter student ID to view: ").strip()
            student = next((s for s in self.students if s.id == student_id), None)
            if student:
                print("\nStudent Information:")
                print("-" * 50)
                print(f"ID: {student.id}")
                print(f"Name: {student.name}")
                print(f"GPA: {student.gpa:.2f}")
            else:
                print("No student found with this ID!")
        except Exception as e:
            print(f"Error viewing student: {e}")

    def plot_gpa_chart(self):
        try:
            if not self.students:
                print("Student list is empty, cannot plot chart!")
                return

            names = [s.name for s in self.students]
            gpas = [s.gpa for s in self.students]

            plt.figure(figsize=(10, 6))
            plt.bar(names, gpas, color='#4CAF50')
            plt.xlabel('Student Name')
            plt.ylabel('GPA')
            plt.title('Student GPA Chart')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Chart plotting error: {e}")

def main():
    manager = StudentManager()
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Display Excellent Students (GPA >=8)")
        print("4. Save to File")
        print("5. View Student by ID")
        print("6. Plot GPA Chart")
        print("7. Exit Program")

        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.display_all_students()
            elif choice == "3":
                manager.display_excellent_students()
            elif choice == "4":
                manager.save_to_file()
            elif choice == "5":
                manager.view_student_by_id()
            elif choice == "6":
                manager.plot_gpa_chart()
            elif choice == "7":
                print("Program terminated!")
                break
            else:
                print("Invalid choice! Please select 1-7.")
        except Exception as e:
            print(f"Program error: {e}")

if __name__ == "__main__":
    main()