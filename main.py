import ustils.util
from core.models import Employee
from database import init_db, SessionLocal
from repository.category_repository import CategoryRepository
from repository.employee_repository import EmployeeRepository
from repository.suppliers_repository import SuppliersRepository
from service.category_service import CategoryService
from service.employee_service import EmployeeService
from service.suppliers_service import SuppliersService


def main():
    # init_db()

    session = SessionLocal()
    emp_repository = EmployeeRepository(session)
    cat_repository = CategoryRepository(session)
    supp_repository = SuppliersRepository(session)
    emp_service = EmployeeService(emp_repository)
    cat_service = CategoryService(cat_repository)
    supp_service = SuppliersService(supp_repository)

    list_employee = ustils.util.generate_employee(0)
    list_category = ustils.util.generate_category(10)
    list_suppliers = ustils.util.generate_suppliers(5)

    for employee in list_employee:
        emp_service.create_employee(employee)

    for supplier in list_suppliers:
        supp_service.create_suppliers(supplier)

    for category in list_category:
        cat_service.create(category)

    employees = emp_service.get_all_employees()
    categories = cat_service.get_all()
    suppliers = supp_repository.get_all()
    #
    # for employee in employees:
    #     print(employee)
    #
    # for category in categories:
    #     print(category)
    #
    # for supplier in suppliers:
    #     print(supplier)



    # suppliers = supplier_service.get_all_suppliers()
    #
    # for supplier in suppliers:
    #     print(supplier)

    # employee_repository = EmployeeRepository(session)
    # employee_service = EmployeeService(employee_repository)
    #
    # first_name = input("Enter your first name: ")
    # last_name = input("Enter your last name: ")
    # email = input("Enter your email address: ")
    # position = input("Enter your position: ")
    # phone = input("Enter your phone number: ")
    #
    # employee_service.create_employee(
    #     first_name=first_name,
    #     last_name=last_name,
    #     email=email,
    #     position=position,
    #     phone=phone
    # )
    #
    # print(f"Employee created successfully:")


if __name__ == '__main__':
    main()