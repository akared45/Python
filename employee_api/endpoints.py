from fastapi import FastAPI, HTTPException, Depends
from models import Employee
from database import Database
from schemas import EmployeeCreate, EmployeeResponse
from typing import List

app = FastAPI()

def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Database = Depends(get_db)):
    new_employee = Employee(
        firstname=employee.firstname,
        middlename=employee.middlename,
        lastname=employee.lastname,
        birthday=employee.birthday,
        phone=employee.phone,
        email=employee.email
    )
    created = db.create_employee(new_employee)
    return created

@app.get("/employees/", response_model=List[EmployeeResponse])
def read_employees(db: Database = Depends(get_db)):
    return db.get_all_employees()

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def read_employee(employee_id: int, db: Database = Depends(get_db)):
    employee = db.get_employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int, 
    employee: EmployeeCreate, 
    db: Database = Depends(get_db)
):
    existing = db.get_employee_by_id(employee_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    updated_employee = Employee(
        id=employee_id,
        firstname=employee.firstname,
        middlename=employee.middlename,
        lastname=employee.lastname,
        birthday=employee.birthday,
        phone=employee.phone,
        email=employee.email
    )
    return db.update_employee(updated_employee)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Database = Depends(get_db)):
    if not db.delete_employee(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}