
from database import init_db, SessionLocal
from repository.category_repository import CategoryRepository
from service.category_service import CategoryService


def main():
    # init_db()

    session = SessionLocal()
    category_repository = CategoryRepository(session)
    category_service = CategoryService(category_repository)

    name_category = input("Enter name of category: ")
    description = input("Enter description: ")

    category_service.create(name_category, description)

    print(f"category {name_category} created")

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