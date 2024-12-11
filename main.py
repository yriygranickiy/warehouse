from core.base_repository import EmployeeRepository, CategoryRepository, OrderRepository, ProductRepository, \
    SuppliersRepository, WarehouseRepository, WarehouseTransactionRepository
from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService, WarehouseTransactionService
from database import init_db, SessionLocal
from core.base_view import EmployeeView, CategoryView, OrderView, ProductView, SuppliersView, WarehouseView, \
    TransactionView

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
            repository = EmployeeRepository(session)
            service = EmployeeService(repository)
            view = EmployeeView(service)
            view.get_view_all()
        elif choice == "2":
            repository = CategoryRepository(session)
            service = CategoryService(repository)
            category_view = CategoryView(service)
            category_view.get_view_all()
        elif choice == "3":
            repository = OrderRepository(session)
            service = OrderService(repository)
            order_view = OrderView(service)
            order_view.get_view_all()
        elif choice == "4":
            repository = ProductRepository(session)
            service = ProductService(repository)
            view = ProductView(service)
            view.get_view_all()
        elif choice == "5":
            repository = SuppliersRepository(session)
            service = SupplierService(repository)
            suppliers_view = SuppliersView(service)
            suppliers_view.get_view_all()
        elif choice == "6":
            repository = WarehouseRepository(session)
            service = WarehouseService(repository)
            warehouse_view = WarehouseView(service)
            warehouse_view.get_view_all()
        elif choice == "7":
            repository = WarehouseTransactionRepository(session)
            service = WarehouseTransactionService(repository)
            transaction_view = TransactionView(service)
            transaction_view.get_view_all()
        elif choice == "8":
            loop_program = False
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
