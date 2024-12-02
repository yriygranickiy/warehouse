from abc import abstractmethod
from typing import Type, Optional, List, TypeVar, Protocol, Generic

from pyexpat import model

from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm import Session

from core.logging_config import logger
from core.models import Category, Employee, Order, Product, Suppliers, Warehouse, WarehouseTransaction

T = TypeVar('T')

class Repository(Protocol, Generic[T]):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        ...

    @abstractmethod
    def create(self, obj: T) -> T:
        ...

    @abstractmethod
    def update(self,obj_id: int, obj: T) -> T:
        ...

    @abstractmethod
    def get_all(self) -> List[T]:
        ...

    @abstractmethod
    def delete(self, id: int):
        ...


class BaseRepository(Repository[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_by_id(self, id: int) -> Optional[T]:
        logger.debug(f'method get_by_id in repository')
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, obj: T) -> T:
        logger.debug(f'method create in repository')
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

    def update(self, model, obj_id: int, obj: T):
        logger.debug(f'method update in repository {model}, with id {obj_id}, using data {obj}')
        try:
            updated_obj = self.db.query(self.model).filter(self.model.id == obj_id).one()
            for key in vars(obj):
                if key.startswith("_"):
                    continue
                new_value = getattr(obj, key)
                if hasattr(updated_obj, key) and new_value is not None:
                    setattr(updated_obj, key, new_value)

            self.db.commit()
        except NoResultFound:
            logger.error(f'Method update in repository {model}, with id {obj_id} not found')
        except SQLAlchemyError as e:
            logger.error(f'Method update in repository {model}, with id {obj_id} failed : {e}')
            self.db.rollback()
            raise

    def get_all(self) -> List[T]:
        logger.debug(f'method get_all in repository')
        return self.db.query(self.model).all()

    def delete(self, id: int):
        logger.debug(f'method delete in repository')
        model = self.get_by_id(id)
        self.db.delete(model)
        self.db.commit()

class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: Session):
        super().__init__(session,Category)

class EmployeeRepository(BaseRepository[Employee]):
    def __init__(self, session: Session):
        super().__init__(session, Employee)

class OrderRepository(BaseRepository[Order]):
    def __init__(self, session: Session):
        super().__init__(session,Order)

class ProductRepository(BaseRepository[Product]):
    def __init__(self, session: Session):
        super().__init__(session,Product)

class SuppliersRepository(BaseRepository[Suppliers]):
    def __init__(self, session: Session):
        super().__init__(session,Suppliers)

class WarehouseRepository(BaseRepository[Warehouse]):
    def __init__(self, session: Session):
        super().__init__(session,Warehouse)

class WarehouseTransactionRepository(BaseRepository[WarehouseTransaction]):
    def __init__(self, session: Session):
        super().__init__(session,WarehouseTransaction)

