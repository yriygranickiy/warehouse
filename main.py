import time

from core.models import Employee
from ustils import generator
from core.base_repository import EmployeeRepository, CategoryRepository, OrderRepository, ProductRepository, \
    SuppliersRepository, WarehouseRepository, WarehouseTransactionRepository
from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService, WarehouseTransactionService
from database import init_db, SessionLocal

init_db()
session = SessionLocal()
def main():

    loop_program = True

    while loop_program:
        print("\nMenu:\n")
        print("1. Employee")
        print("2. Category")
        print("3. Order")
        print("4. Product")
        print("5. Suppliers")
        print("6. Warehouse")
        print("7. Transaction")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            employee_choice()

        elif choice == "2":
            category_repository = CategoryRepository(session)
            category_service = CategoryService(repository=category_repository)
            list_category = category_service.get_all()
            for category in list_category:
                print(category)

        elif choice == "3":
            order_repository = OrderRepository(session)
            order_service = OrderService(repository=order_repository)
            for order in order_service.get_all():
                print(order)

        elif choice == "4":
            product_repository = ProductRepository(session)
            product_service = ProductService(repository=product_repository)
            for product in product_service.get_all():
                print(product)

        elif choice == "5":
            suppliers_repository = SuppliersRepository(session)
            supplier_service = SupplierService(repository=suppliers_repository)
            for supplier in supplier_service.get_all():
                print(supplier)

        elif choice == "6":
            warehouse_repository = WarehouseRepository(session)
            warehouse_service = WarehouseService(repository=warehouse_repository)
            for warehouse in warehouse_service.get_all():
                print(warehouse)

        elif choice == "7":
            transaction_repository = WarehouseTransactionRepository(session)
            transaction_service = WarehouseTransactionService(repository=transaction_repository)
            for transaction in transaction_service.get_all():
                print(transaction)

        elif choice == "8":
            loop_program = False
        else:
            print("Invalid choice")


def employee_choice():
    employee_repository = EmployeeRepository(session)
    employee_service = EmployeeService(repository=employee_repository)

    employee_loop_menu = True
    while employee_loop_menu:
        print("\nEmployee:\n")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Get all")
        print("5. Get employee by id")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number: ")
            created_employee = Employee(first_name=first_name,
                                        last_name=last_name,
                                        position="staff",
                                        email=email,
                                        phone=phone)
            print("Employee adding....")
            employee_service.create(created_employee)
            time.sleep(0.3)
            print("Employee add successfully!")
        elif choice == "2":
            print("Input employee id for deleting")
            employee_id = input("Enter employee id: ")
            print("Deleting employee...")
            time.sleep(0.3)
            employee_service.delete(employee_id)
            print("Employee delete successfully!")
        elif choice == "3":
            pass
        elif choice == "4":
            print("load list employee...")
            time.sleep(0.3)
            for employee in employee_service.get_all():
                print(employee)
                time.sleep(0.3)
            print("list load successfully!")
        elif choice == "5":
            employee_id = input("Enter employee id: ")
            employee = employee_service.get_by_id(employee_id)
            print("getting employee data...")
            time.sleep(0.3)
            print(employee)
            print("employee data get successfully!")
        elif choice == "6":
            employee_loop_menu = False
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
