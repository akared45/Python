from typing import List
from .models import Student

class StudentRepository:
    def add_student(self, student):
        raise NotImplementedError
    
    def get_all_students(self):
        raise NotImplementedError
    
    def get_students_older_than(self, age):
        raise NotImplementedError
    
    def get_students_with_gpa_and_age(self, min_gpa, max_gpa, max_age):
        raise NotImplementedError
    
    def save_to_file(self, filename):
        raise NotImplementedError