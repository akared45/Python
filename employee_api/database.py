import mysql.connector
from dotenv import load_dotenv
import os
from datetime import date
from models import Employee

load_dotenv()

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    
    def get_all_employees(self) -> list[Employee]:
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees")
        employees = []
        for row in cursor:
            employees.append(self._row_to_employee(row))
        cursor.close()
        return employees
    
    def get_employee_by_id(self, id: int) -> Employee:
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return self._row_to_employee(row)
        return None
    
    def create_employee(self, employee: Employee) -> Employee:
        cursor = self.connection.cursor()
        query = """
            INSERT INTO employees 
            (firstname, middlename, lastname, birthday, phone, email) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            employee.firstname,
            employee.middlename,
            employee.lastname,
            employee.birthday,
            employee.phone,
            employee.email
        )
        cursor.execute(query, values)
        self.connection.commit()
        employee.id = cursor.lastrowid
        cursor.close()
        return employee
    
    def update_employee(self, employee: Employee) -> Employee:
        cursor = self.connection.cursor()
        query = """
            UPDATE employees SET 
            firstname = %s, middlename = %s, lastname = %s, 
            birthday = %s, phone = %s, email = %s 
            WHERE id = %s
        """
        values = (
            employee.firstname,
            employee.middlename,
            employee.lastname,
            employee.birthday,
            employee.phone,
            employee.email,
            employee.id
        )
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()
        return employee
    
    def delete_employee(self, id: int) -> bool:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
        affected_rows = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return affected_rows > 0
    
    def _row_to_employee(self, row) -> Employee:
        return Employee(
            id=row['id'],
            firstname=row['firstname'],
            middlename=row['middlename'],
            lastname=row['lastname'],
            birthday=row['birthday'],
            phone=row['phone'],
            email=row['email']
        )
    
    def close(self):
        self.connection.close()