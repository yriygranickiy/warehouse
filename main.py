from core.models import Employee
from database import init_db, SessionLocal
from repository.employee_repository import EmployeeRepository
from service.employee_service import EmployeeService


def main():
    # init_db()

    session = SessionLocal()
    employee_repository = EmployeeRepository(session)
    employee_service = EmployeeService(employee_repository)

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    position = input("Enter your position: ")
    phone = input("Enter your phone number: ")

    employee_service.create_employee(
        first_name=first_name,
        last_name=last_name,
        email=email,
        position=position,
        phone=phone
    )

    print(f"Employee created successfully:")


if __name__ == '__main__':
    main()