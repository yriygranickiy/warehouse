
from core.base_repository import EmployeeRepository, CategoryRepository, OrderRepository, ProductRepository, \
    SuppliersRepository, WarehouseRepository, WarehouseTransactionRepository
from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService, WarehouseTransactionService
from database import init_db, SessionLocal
from core.base_view import EmployeeView, CategoryView, OrderView, ProductView, SuppliersView, WarehouseView, \
    TransactionView

init_db()
session = SessionLocal()


def handle_choice(choice):
    options = {
        '1': ('Employee', EmployeeRepository, EmployeeService, EmployeeView),
        '2': ('Category', CategoryRepository, CategoryService, CategoryView),
        '3': ('Order', OrderRepository, OrderService, OrderView),
        '4': ('Product', ProductRepository, ProductService, ProductView),
        '5': ('Supplier', SuppliersRepository, SupplierService, SuppliersView),
        '6': ('Warehouse', WarehouseRepository, WarehouseService, WarehouseView),
        '7': ('Transaction', WarehouseTransactionRepository, WarehouseTransactionService, TransactionView)
    }
    if choice in options:
        entity_name, repository, service, view = options[choice]
        rep = repository(session)
        serv = service(rep)
        views = view(serv)
        views.get_view_all()
    elif choice == "8":
        return False
    else:
        print("Invalid choice")
    return True


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

        loop_program = handle_choice(choice)


if __name__ == '__main__':
    main()
