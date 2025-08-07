from domain.models import Student
from domain.repository import StudentRepository

class StudentService:
    def __init__(self, repository):
        self._repo = repository
    
    def add_student(self, student):
        self._repo.add_student(student)
    
    def get_all_students(self):
        return self._repo.get_all_students()
    
    def get_students_older_than(self, age):
        return self._repo.get_students_older_than(age)
    
    def get_high_gpa_young_students(self):
        return self._repo.get_students_with_gpa_and_age(8.0, 10.0, 22)
    
    def save_data(self, filename):
        self._repo.save_to_file(filename)
    
    def load_data(self, filename):
        if hasattr(self._repo, 'load_from_file'):
            self._repo.load_from_file(filename)
