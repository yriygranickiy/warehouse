import ustils.util
from core.models import Employee
from database import init_db, SessionLocal
from repository.category_repository import CategoryRepository
from repository.employee_repository import EmployeeRepository
from repository.order_repository import OrderRepository
from repository.product_repository import ProductRepository
from repository.suppliers_repository import SuppliersRepository
from repository.warehouse_transaction_repository import WarehouseTransactionRepository
from repository.wearhouse_repository import WarehouseRepository
from service.category_service import CategoryService
from service.employee_service import EmployeeService
from service.order_service import OrderService
from service.product_service import ProductService
from service.suppliers_service import SuppliersService
from service.warehouse_service import WarehouseService
from service.warehouse_transaction_service import WarehouseTransactionService


def main():
    init_db()

    session = SessionLocal()
    emp_repository = EmployeeRepository(session)
    cat_repository = CategoryRepository(session)
    supp_repository = SuppliersRepository(session)
    prod_repository = ProductRepository(session)
    warehouse_repository = WarehouseRepository(session)
    warehouse_transaction_repository = WarehouseTransactionRepository(session)
    order_repository = OrderRepository(session)

    emp_service = EmployeeService(emp_repository)
    cat_service = CategoryService(cat_repository)
    supp_service = SuppliersService(supp_repository)
    prod_service = ProductService(prod_repository)
    warehouse_service = WarehouseService(warehouse_repository)
    warehouse_transaction_service = WarehouseTransactionService(warehouse_transaction_repository)
    order_service = OrderService(order_repository)

    # list_employee = ustils.util.generate_employee(40)
    # list_category = ustils.util.generate_category(20)
    # list_suppliers = ustils.util.generate_suppliers(10)
    # list_product = ustils.util.generate_product(33)
    # list_warehouse = ustils.util.generate_warehouse(5)
    # list_warehouse_transaction = ustils.util.generate_warehouse_transaction(75)
    list_order = ustils.util.generate_order(75)

    # for employee in list_employee:
    #     emp_service.create_employee(employee)

    # for supplier in list_suppliers:
    #     supp_service.create_suppliers(supplier)
    #
    # for category in list_category:
    #     cat_service.create(category)

    # for product in list_product:
    #     prod_service.create_product(product)
    #
    # for warehouse in list_warehouse:
    #     warehouse_service.add(warehouse)

    # for warehouse_transaction in list_warehouse_transaction:
    #     warehouse_transaction_service.add(warehouse_transaction)

    for order in list_order:
        order_service.add_order(order)


    # employees = emp_service.get_all_employees()
    # categories = cat_service.get_all()
    # suppliers = supp_service.get_all_suppliers()
    #
    # pod_list = prod_service.get_all_products()
    #
    # for pod in pod_list:
    #     print(pod)

    # for employee in employees:
    #     print(employee)

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