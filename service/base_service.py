from abc import abstractmethod
from typing import Generic, List, TypeVar, Protocol

from core.models import Category, Employee, Order, Product, Suppliers, Warehouse, WarehouseTransaction
from repository.base_repository import Repository
from repository.category_repository import CategoryRepository
from repository.employee_repository import EmployeeRepository
from repository.order_repository import OrderRepository
from repository.product_repository import ProductRepository
from repository.suppliers_repository import SuppliersRepository
from repository.wearhouse_repository import WarehouseRepository

T = TypeVar('T')
class Service(Protocol,Generic[T]):

    @abstractmethod
    def get_by_id(self, id: int) -> T:
        ...
    @abstractmethod
    def create(self, obj: T) -> T:
        ...
    @abstractmethod
    def get_all(self)->List[T]:
        ...

class BaseService(Service[T], Generic[T]):
    def __init__(self, repository: Repository[T]):
        self.repository = repository

    def get_by_id(self, id: int) -> T:
        return self.repository.get_by_id(id)

    def create(self, data: T) -> T:
        self.repository.create(data)

    def get_all(self) -> List[T]:
        return self.repository.get_all()


class CategoryService(BaseService[Category]):
    def __init__(self, repository: CategoryRepository):
        super().__init__(repository)

class EmployeeService(BaseService[Employee]):
    def __init__(self, repository: EmployeeRepository):
        super().__init__(repository)

class OrderService(BaseService[Order]):
    def __init__(self, repository: OrderRepository):
        super().__init__(repository)

class ProductService(BaseService[Product]):
    def __init__(self, repository: ProductRepository):
        super().__init__(repository)

class SupplierService(BaseService[Suppliers]):
    def __init__(self, repository: SuppliersRepository):
        super().__init__(repository)

class WarehouseService(BaseService[Warehouse]):
    def __init__(self, repository: WarehouseRepository):
        super().__init__(repository)

class WarehouseTransactionRepository(BaseService[WarehouseTransaction]):
    def __init__(self, repository: WarehouseRepository):
        super().__init__(repository)

