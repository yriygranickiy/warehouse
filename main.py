from datetime import datetime, date

import ustils.util
from core.models import Employee, Order
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

    order_repository = OrderRepository(session)
    order_service = OrderService(order_repository)

    employee_repository = EmployeeRepository(session)
    employee_service = EmployeeService(employee_repository)

    list_orders = order_service.get_all()

    for order in list_orders:
        print(order)


if __name__ == '__main__':
    main()
