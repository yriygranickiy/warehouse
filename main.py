import time

from ustils import generator
from core.base_repository import EmployeeRepository, CategoryRepository, OrderRepository, ProductRepository, \
    SuppliersRepository, WarehouseRepository, WarehouseTransactionRepository
from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService, WarehouseTransactionService
from database import init_db, SessionLocal


def main():

    init_db()
    session = SessionLocal()
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
        print()

        if choice == "1":
            employee_repository = EmployeeRepository(session)
            employee_service = EmployeeService(repository=employee_repository)
            list_employee = employee_service.get_all()

            print("load data employee...")
            time.sleep(3)
            print("list all employee: ")

            for employee in list_employee:
                time.sleep(0.3)
                print(employee)


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








if __name__ == '__main__':
    main()
