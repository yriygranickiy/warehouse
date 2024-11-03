
from database import init_db, SessionLocal
from repository.category_repository import CategoryRepository
from repository.suppliers_repository import SuppliersRepository
from service.category_service import CategoryService
from service.suppliers_service import SuppliersService


def main():
    # init_db()

    session = SessionLocal()
    repository = SuppliersRepository(session)
    service = SuppliersService(repository)

    name_supplier = input("Enter name of supplier: ")
    contact_person = input("Enter contact person: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    service.create_suppliers(name_supplier, contact_person, phone_number, email, address)

    print(f"supplier {name_supplier} created ")

    suppliers = service.get_all_suppliers()

    for supplier in suppliers:
        print(supplier)

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