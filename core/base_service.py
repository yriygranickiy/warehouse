from abc import abstractmethod, ABC
from typing import List, TypeVar, Generic

from core.logging_config import logger
from core.base_repository import Repository, WarehouseRepository, WarehouseTransactionRepository, \
    SuppliersRepository, ProductRepository, OrderRepository, EmployeeRepository, CategoryRepository
from core.models import Product

T = TypeVar('T')


class Service(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def create(self, obj: T):
        raise NotImplementedError

    @abstractmethod
    def update(self, model, model_id: int, obj: T):
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int):
        raise NotImplementedError

class BaseService(Service):
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_by_id(self, id: int) -> T:
        logger.info("method get_by_id called in service")
        return self.repository.get_by_id(id)

    def create(self, data: T):
        logger.info("method create called in service")
        self.repository.create(data)

    def update(self, model_id: int, data: T):
        logger.info("Method UPDATE called in service")
        try:
            update_model = self.repository.update( model_id, data)
            if update_model:
                logger.debug(f'Successfully updated')
            else:
                print(f'Object this id {model_id} is not found')
        except Exception as e:
            logger.error(f'Service error during update: {e}')
            print(f'Error:{str(e)}')

        self.repository.update(model_id, data)

    def get_all(self) -> List[T]:
        logger.info("method get_all called in service")
        return self.repository.get_all()

    def delete(self, id: int):
        logger.info("method delete called in service")
        self.repository.delete(id)


class CategoryService(BaseService):
    def __init__(self, repository: CategoryRepository):
        super().__init__(repository)


class EmployeeService(BaseService):
    def __init__(self, repository: EmployeeRepository):
        super().__init__(repository)


class OrderService(BaseService):
    def __init__(self, repository: OrderRepository):
        super().__init__(repository)


class ProductService(BaseService):
    def __init__(self, repository: ProductRepository):
        super().__init__(repository)
        self.repository = repository

    def get_product_with_details(self):

        list_product = self.repository.get_product_with_details()

        return list_product

class SupplierService(BaseService):
    def __init__(self, repository: SuppliersRepository):
        super().__init__(repository)


class WarehouseService(BaseService):
    def __init__(self, repository: WarehouseRepository):
        super().__init__(repository)


class WarehouseTransactionService(BaseService):
    def __init__(self, repository: WarehouseTransactionRepository):
        super().__init__(repository)
