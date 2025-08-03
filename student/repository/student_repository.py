from domain.student import Student

class StudentRepository:
    def __init__(self):
        self.students = []
    
    def add(self, student : Student):
        self.students.append(student)

    def get_all(self) -> list[Student]:
        return self.students
    
    def filter_by_age(self, min_age) -> list[Student]:
        return[student for student in self.students 
               if student.get_age() > min_age]
    
    def filter_by_gpa_and_age(self, min_gpa: float, max_gpa: float, max_age: int) -> list[Student]:
        return [student for student in self.students 
                if min_gpa <= student.gpa <= max_gpa and student.get_age() < max_age]
    
    def save_to_file(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            for student in self.students:
                f.write(f"{student.regno},{student.firstname},{student.middlename},{student.lastname},"
                        f"{student.birthday.strftime('%Y-%m-%d')},{student.address},{student.phone},{student.gpa}\n")