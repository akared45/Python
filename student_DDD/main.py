from infrastructure.persistence import FileStudentRepository
from application.services import StudentService
from presentation.ui import StudentMenu

def main():
    repository = FileStudentRepository()
    service = StudentService(repository)
    
    try:
        service.load_data("students.dat")
    except FileNotFoundError:
        pass

    menu = StudentMenu(service)
    menu.run()

if __name__ == "__main__":
    main()