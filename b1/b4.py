class Student:
    def __init__(self, student_id, firstname, middlename, lastname, birthday):
        self.student_id = student_id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday

    def displayinfo(self):
        full_name = f"{self.firstname} {self.middlename} {self.lastname}"
        print(f"Student ID: {self.student_id}")
        print(f"Full Name: {full_name}")
        print(f"Birthday: {self.birthday}")

if __name__ == "__main__":
    student1 = Student(
        student_id="S001",
        firstname="Nguyen",
        middlename="Van",
        lastname="An",
        birthday="2003-05-12"
    )
    
    student1.displayinfo()
