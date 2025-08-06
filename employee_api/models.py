from datetime import date

class Employee:
    def __init__(self, id, firstname, middlename, lastname, birthday, phone, email):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday
        self.phone = phone
        self.email = email