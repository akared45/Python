from datetime import datetime
from domain.person import Person

class Student(Person):
    def __init__(self, firstname, middlename, lastname, birthday, address, phone, regno, gpa):
        super().__init__(firstname, middlename, lastname, birthday, address, phone)
        self.regno = regno
        self.gpa = gpa

    def __repr__(self) -> str:
        return (f"Student(regno='{self.regno}', gpa={self.gpa}, "
                f"firstname='{self.firstname}', middlename='{self.middlename}', "
                f"lastname='{self.lastname}', birthday={self.birthday}, "
                f"address='{self.address}', phone='{self.phone}')")