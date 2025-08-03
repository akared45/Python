from datetime import datetime

class Person:
    def __init__(self, firstname, middlename, lastname, birthday, address, phone):
        self.firstname  = firstname
        self.middlename = middlename
        self.lastname   = lastname
        self.birthday   = birthday
        self.address    = address
        self.phone      = phone
    
    def get_fullname(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"

    def get_age(self):
        today = datetime.now()
        age = today.year - self.birthday.year
        if(today.month < self.birthday.month or 
          (today.month == self.birthday.month and today.day < self.birthday.day)
        ):
            age -= 1
        return age
    
    def __repr__(self):
         return (f"Person(firstname='{self.firstname}', middlename='{self.middlename}', "
                f"lastname='{self.lastname}', birthday={self.birthday}, "
                f"address='{self.address}', phone='{self.phone}')")