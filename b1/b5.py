class Student:
    def __init__(self, student_id, firstname, middlename, lastname, birthday, grades):
        self.student_id = student_id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def displayInfo(self, context="Student"):
        full_name = f"{self.firstname} {self.middlename} {self.lastname}"
        avg = self.average_grade()
        student_info = f"Name: {full_name}, Average Grade: {avg:.2f}, Birthday: {self.birthday}"
        return f"{context}: {student_info}"

def find_highest_average(students):
    if not students:
        return None
    return max(students, key=lambda s: s.average_grade())

def filter_high_achievers(students, threshold=8.0):
    return list(filter(lambda s: s.average_grade() > threshold, students))

if __name__ == "__main__":
    students = [
        Student(student_id="S001", firstname="Nguyen", middlename="Van", lastname="An", birthday="2003-05-12", grades=[9.2, 8.5, 10.0]), 
        Student(student_id="S002", firstname="Tran", middlename="Thi", lastname="Binh", birthday="2002-11-30", grades=[7.0, 7.2, 6.8]),  
        Student(student_id="S003", firstname="Le", middlename="Hoang", lastname="Cuong", birthday="2004-03-25", grades=[6.0, 7.0, 7.5]),  
        Student(student_id="S004", firstname="Pham", middlename="Minh", lastname="Dung", birthday="2003-08-17", grades=[8.9, 9.1, 8.7]),  
        Student(student_id="S005", firstname="Hoang", middlename="Kim", lastname="Anh", birthday="2001-09-02", grades=[9.5, 9.8, 10.0]),  
    ]

    top_student = find_highest_average(students)
    if top_student:
        print(top_student.displayInfo(context="\nStudent with Highest Grades"))

    high_achievers = filter_high_achievers(students)
    print("\nStudents with Average Grade > 8:")
    for student in high_achievers:
        print(student.displayInfo(context="High Achieving Student"))