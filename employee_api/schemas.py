from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    birthday: date
    phone: str
    email: str

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True