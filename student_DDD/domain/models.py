import datetime

class Person:
    def __init__(self, firstname, middlename, lastname, 
                 birthday, address, phone):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday
        self.address = address
        self.phone = phone
    
    def get_fullname(self):
        return f"{self.lastname} {self.middlename} {self.firstname}"
    
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age


class Student(Person):
    def __init__(self, firstname, middlename, lastname, 
                 birthday, address, phone, 
                 regno, gpa):
        super().__init__(firstname, middlename, lastname, birthday, address, phone)
        self.regno = regno
        self.gpa = gpa
    
    def __str__(self):
        return (f"{self.regno}: {self.get_fullname()} - "
                f"GPA: {self.gpa} - Age: {self.get_age()}")