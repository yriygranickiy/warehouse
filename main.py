import random
import time
from datetime import datetime
from core.models import Employee, Category, Order, Product, Suppliers, Warehouse, WarehouseTransaction
from core.base_repository import EmployeeRepository, CategoryRepository, OrderRepository, ProductRepository, \
    SuppliersRepository, WarehouseRepository, WarehouseTransactionRepository
from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService, WarehouseTransactionService
from database import init_db, SessionLocal
from core.base_view import EmployeeView

init_db()
session = SessionLocal()


# TODO: create method update for all models!!!

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
            repository = EmployeeRepository(session)
            service = EmployeeService(repository)
            EmployeeView.get_view_all(service)
            # employee_view()
        elif choice == "2":
            category_view()
        elif choice == "3":
            order_view()
        elif choice == "4":
            product_view()
        elif choice == "5":
            suppliers_view()
        elif choice == "6":
            warehouse_view()
        elif choice == "7":
            transaction_view()
        elif choice == "8":
            loop_program = False
        else:
            print("Invalid choice")


# def employee_view():
#     employee_repository = EmployeeRepository(session)
#     employee_service = EmployeeService(repository=employee_repository)
#
#     employee_loop_menu = True
#     while employee_loop_menu:
#         print("\nEmployee:\n")
#         print("1. Add")
#         print("2. Delete")
#         print("3. Update")
#         print("4. Get all")
#         print("5. Get employee by id")
#         print("6. Exit")
#
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             first_name = input("Enter your first name: ")
#             last_name = input("Enter your last name: ")
#             email = input("Enter your email: ")
#             phone = input("Enter your phone number: ")
#             created_employee = Employee(first_name=first_name,
#                                         last_name=last_name,
#                                         position="staff",
#                                         email=email,
#                                         phone=phone)
#             print("Employee adding....")
#             employee_service.create(created_employee)
#             time.sleep(0.3)
#             print("Employee add successfully!")
#         elif choice == "2":
#             print("Input employee id for deleting")
#             employee_id = int(input("Enter employee id: "))
#             print("Deleting employee...")
#             time.sleep(0.3)
#             employee_service.delete(employee_id)
#             print("Employee delete successfully!")
#         elif choice == "3":
#             pass
#         elif choice == "4":
#             print("load list employee...")
#             time.sleep(0.3)
#             for employee in employee_service.get_all():
#                 print(employee)
#                 time.sleep(0.3)
#             print("list load successfully!")
#         elif choice == "5":
#             employee_id = input("Enter employee id: ")
#             employee = employee_service.get_by_id(employee_id)
#             print("getting employee data...")
#             time.sleep(0.3)
#             print(employee)
#             print("employee data get successfully!")
#         elif choice == "6":
#             employee_loop_menu = False
#         else:
#             print("Invalid choice")


def category_view():
    category_repository = CategoryRepository(session)
    category_service = CategoryService(repository=category_repository)

    category_loop_menu = True
    while category_loop_menu:
        print("\nCategory:\n")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Get all")
        print("5. Get category by id")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            category_name = input("Enter name: ")
            category_desc = input("Enter description: ")
            created_category = Category(category_name=category_name,
                                        description=category_desc)
            print("Category adding....")
            time.sleep(0.3)
            category_service.create(created_category)
            print("Category add successfully!")
        elif choice == "2":
            category_id = int(input("Enter category id: "))
            print("Deleting category...")
            time.sleep(0.3)
            category_service.delete(category_id)
            print("Category delete successfully!")
        elif choice == "3":
            pass
        elif choice == "4":
            print("Load list category...")
            time.sleep(0.3)
            for category in category_service.get_all():
                print(category)
                time.sleep(0.3)
            print("list load successfully!")
        elif choice == "5":
            category_id = int(input("Enter category id: "))
            category = category_service.get_by_id(category_id)
            print("Getting category data...")
            time.sleep(0.3)
            print(category)
            print("category data get successfully!")
        elif choice == "6":
            category_loop_menu = False
        else:
            print("Invalid choice")


def order_view():
    order_repository = OrderRepository(session)
    order_service = OrderService(repository=order_repository)

    order_loop_menu = True
    while order_loop_menu:
        print("\nOrder:\n")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Get all")
        print("5. Get order by id")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            quantity = int(input("Enter quantity: "))
            order = Order(quantity=quantity,
                          order_date=datetime.now(),
                          order_state='Pending',
                          product_id=random.randint(2, 3))
            print("Order adding....")
            time.sleep(0.3)
            order_service.create(order)
            print("Order add successfully!")
        elif choice == "2":
            order_id = int(input("Enter order id: "))
            print("Deleting order...")
            order_service.delete(order_id)
            time.sleep(0.3)
            print("Order delete successfully!")
        elif choice == "3":
            pass
        elif choice == "4":
            print("Load list order...")
            for order in order_service.get_all():
                print(order)
                time.sleep(0.3)
            print("list load successfully!")
        elif choice == "5":
            order_id = int(input("Enter order id: "))
            order = order_service.get_by_id(order_id)
            print("Getting order data...")
            time.sleep(0.3)
            print(order)
            print("Order data get successfully!")
        elif choice == "6":
            order_loop_menu = False
        else:
            print("Invalid choice")


def product_view():
    product_repository = ProductRepository(session)
    product_service = ProductService(repository=product_repository)
    product_loop_menu = True
    while product_loop_menu:
        print("\nProduct:\n")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Get all")
        print("5. Get product by id")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            description = input("Enter description: ")

            product = Product(product_name=product_name,
                              quantity=quantity,
                              price=price,
                              description=description,
                              created_date=datetime.now(),
                              category_id=random.randint(2, 11),
                              supplier_id=random.randint(2, 5))
            print("Product adding....")
            time.sleep(0.3)
            product_service.create(product)
            print("Product add successfully!")
        elif choice == "2":
            product_id = int(input("Enter product id: "))
            print("Deleting product...")
            product_service.delete(product_id)
            print("Product delete successfully!")
        elif choice == "3":
            pass
        elif choice == "4":
            print("Load list product...")
            for product in product_service.get_all():
                print(product)
                time.sleep(0.3)
            print("list load successfully!")
        elif choice == "5":
            product_id = int(input("Enter product id: "))
            print("Getting product data...")
            time.sleep(0.3)
            product = product_service.get_by_id(product_id)
            print(product)
            print("Getting product data...")
        elif choice == "6":
            product_loop_menu = False
        else:
            print("Invalid choice")


def suppliers_view():
    suppliers_repository = SuppliersRepository(session)
    suppliers_service = SupplierService(suppliers_repository)
    suppliers_loop_menu = True
    while suppliers_loop_menu:
        print("\nSuppliers:\n")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Get all")
        print("5. Get suppliers by id")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            supplier_name = input("Enter supplier name: ")
            contact_person = input("Enter contact person: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")

            supplier = Suppliers(supplier_name=supplier_name,
                                 contact_person=contact_person,
                                 phone=phone,
                                 email=email,
                                 address=address)
            print("Supplier adding....")
            time.sleep(0.3)
            suppliers_service.create(supplier)
            print("Supplier add successfully!")
        elif choice == "2":
            supplier_id = int(input("Enter supplier id: "))
            print("Deleting supplier...")
            time.sleep(0.3)
            suppliers_service.delete(supplier_id)
            print("Supplier delete successfully!")
        elif choice == "3":
            pass
        elif choice == "4":
            print("Load list supplier...")
            for supplier in suppliers_service.get_all():
                print(supplier)
                time.sleep(0.3)
            print("list load successfully!")
        elif choice == "5":
            supplier_id = int(input("Enter supplier id: "))
            print("Getting supplier data...")
            supplier = suppliers_service.get_by_id(supplier_id)
            time.sleep(0.3)
            print(supplier)
            print("Getting supplier data...")
        elif choice == "6":
            suppliers_loop_menu = False
        else:
            print("Invalid choice")


def warehouse_view():
    warehouse_repository = WarehouseRepository(session)
    warehouse_service = WarehouseService(warehouse_repository)
    warehouse_loop_menu = True
    while warehouse_loop_menu:
        print("\nWarehouses:\n")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Get all")
        print("5. Get warehouse by id")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            warehouse_name = input("Enter warehouse name: ")
            location = input("Enter location: ")

            warehouse = Warehouse(warehouse_name=warehouse_name,
                                  location=location)
            print("Warehouse adding....")
            time.sleep(0.3)
            warehouse_service.create(warehouse)
            print("Warehouse add successfully!")
        elif choice == "2":
            warehouse_id = int(input("Enter warehouse id: "))
            print("Deleting warehouse...")
            time.sleep(0.3)
            warehouse_service.delete(warehouse_id)
            print("Warehouse delete successfully!")
        elif choice == "3":
            pass
        elif choice == "4":
            print("Load list warehouse...")
            for warehouse in warehouse_service.get_all():
                print(warehouse)
                time.sleep(0.3)
            print("list load successfully!")
        elif choice == "5":
            warehouse_id = int(input("Enter warehouse id: "))
            print("Getting warehouse data...")
            time.sleep(0.3)
            print(warehouse_service.get_by_id(warehouse_id))
            print("Getting warehouse data...")
        elif choice == "6":
            warehouse_loop_menu = False
        else:
            print("Invalid choice")


def transaction_view():
    transaction_repository = WarehouseTransactionRepository(session)
    transaction_service = WarehouseTransactionService(transaction_repository)
    transaction_loop_menu = True
    while transaction_loop_menu:
        print("\nTransactions:\n")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Get all")
        print("5. Get transaction by id")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            quantity = int(input("Enter quantity: "))
            comment = input("Enter comment: ")

            transaction = WarehouseTransaction(quantity=quantity,
                                               transaction_type='purchase',
                                               transaction_date=datetime.now(),
                                               comment=comment,
                                               product_id=random.randint(2, 3),
                                               employee_id=random.randint(1, 2),
                                               warehouse_id=random.randint(1, 2))
            print("Transaction adding....")
            time.sleep(0.3)
            transaction_service.create(transaction)
            print("Transaction add successfully!")
        elif choice == "2":
            transaction_id = int(input("Enter transaction id: "))
            print("Deleting transaction...")
            time.sleep(0.3)
            transaction_service.delete(transaction_id)
            print("Transaction delete successfully!")
        elif choice == "3":
            pass
        elif choice == "4":
            print("Load list transaction...")
            for transaction in transaction_service.get_all():
                print(transaction)
                time.sleep(0.3)
            print("list load successfully!")
        elif choice == "5":
            transaction_id = int(input("Enter transaction id: "))
            print("Getting transaction data...")
            time.sleep(0.3)
            print(transaction_service.get_by_id(transaction_id))
            print("Getting transaction data...")
        elif choice == "6":
            transaction_loop_menu = False
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
