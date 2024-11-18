from abc import abstractmethod
from typing import Generic, List, TypeVar, Protocol
from .logging_config import logger

from core.models import Category, Employee, Order, Product, Suppliers, Warehouse, WarehouseTransaction
from core.base_repository import Repository, WarehouseRepository, WarehouseTransactionRepository, \
    SuppliersRepository, ProductRepository, OrderRepository, EmployeeRepository, CategoryRepository

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
        logger.info("method get_by_id called in service")
        return self.repository.get_by_id(id)

    def create(self, data: T) -> T:
        logger.info("method create called in service")
        self.repository.create(data)

    def get_all(self) -> List[T]:
        logger.info("method get_all called in service")
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

class WarehouseTransactionService(BaseService[WarehouseTransaction]):
    def __init__(self, repository: WarehouseTransactionRepository):
        super().__init__(repository)

