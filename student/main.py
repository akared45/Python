from repository.student_repository import StudentRepository
from service.student_service import StudentService
from application.ui import display_menu, display_students, get_student_input, display_students

def main():
    repository = StudentRepository()
    service = StudentService(repository)

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            student = get_student_input()
            service.add_student(student)
            print("Student added successfully")
            
        elif choice == '2':
            students = service.get_all_students()
            display_students(students)
            
        elif choice == '3':
            students = service.filter_students_above_age(22)
            display_students(students)
            
        elif choice == '4':
            students = service.filter_students_by_gpa_and_age(80, 100, 22)
            display_students(students)
            
        elif choice == '5':
            filename = input("Enter filename to save (e.g., students.txt): ")
            service.save_students_to_file(filename)
            print(f"Students saved to {filename}")
            
        elif choice == '6':
            service.plot_gpa_chart()
            
        elif choice == '7':
            print("Exiting program")
            break
            
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()