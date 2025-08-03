from domain.student import Student
from repository.student_repository import StudentRepository
import matplotlib.pyplot as plt

class StudentService:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def add_student(self, student: Student):
        self.repository.add(student)

    def get_all_students(self) -> list[Student]:
        return self.repository.get_all()
    
    def filter_students_above_age(self, age) -> list[Student]:
        return self.repository.filter_by_age(age)
    
    def filter_students_by_gpa_and_age(self, min_gpa, max_gpa, max_age) -> list[Student]:
        return self.repository.filter_by_gpa_and_age(min_gpa, max_gpa, max_age)

    def save_students_to_file(self, filename: str):
        self.repository.save_to_file(filename)

    def plot_gpa_chart(self):
        students = self.repository.get_all()
        if not students:
            print("No students to display in chart")
            return

        names = [student.get_fullname() for student in students]
        gpas = [student.gpa for student in students]

        plt.figure(figsize=(10, 6))
        plt.bar(names, gpas)
        plt.xlabel('Students')
        plt.ylabel('GPA')
        plt.title('Student GPA Chart')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    