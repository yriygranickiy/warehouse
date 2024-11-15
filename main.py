from core.base_repository import EmployeeRepository
from core.base_service import EmployeeService
from database import init_db, SessionLocal



def main():

    init_db()

    session = SessionLocal()

    employee_repository = EmployeeRepository(session)
    employee_service = EmployeeService(employee_repository)

    list_employee = employee_service.get_all()

    for employee in list_employee:
        print(employee)


if __name__ == '__main__':
    main()
