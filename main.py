from ustils import generator
from core.base_repository import EmployeeRepository
from core.base_service import EmployeeService
from database import init_db, SessionLocal




def main():

    init_db()

    session = SessionLocal()

    # employee_repository = EmployeeRepository(session)
    # employee_service = EmployeeService(employee_repository)

    suppliers_repository = EmployeeRepository(session)
    suppliers_service = EmployeeService(suppliers_repository)


    # list_suppliers = generator.generate_suppliers(20)

    list_suppliers = suppliers_service.get_all()

    for supplier in list_suppliers:
        print(supplier)

    # list_emolyees_created = ustils.generator.generate_employee(20)
    #
    # for employee in list_emolyees_created:
    #     employee_service.create(employee)

    # list_employee = employee_service.get_all()
    #
    # for employee in list_employee:
    #     print(employee)


if __name__ == '__main__':
    main()
