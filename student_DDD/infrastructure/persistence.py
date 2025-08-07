import pickle
import os
from domain.models import Student
from domain.repository import StudentRepository

class FileStudentRepository(StudentRepository):
    def __init__(self):
        self._students = []
    
    def add_student(self, student):
        self._students.append(student)
    
    def get_all_students(self):
        return self._students.copy()
    
    def get_students_older_than(self, age):
        return [s for s in self._students if s.get_age() > age]
    
    def get_students_with_gpa_and_age(self, min_gpa, max_gpa, max_age):
        return [s for s in self._students 
                if min_gpa <= s.gpa <= max_gpa and s.get_age() < max_age]
    
    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self._students, f)
    
    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self._students = pickle.load(f)
