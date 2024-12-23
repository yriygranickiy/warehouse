from abc import abstractmethod, ABC
from typing import Type, Optional, List, TypeVar, Generic

from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from core.logging_config import logger
from core.models import Category, Employee, Order, Product, Suppliers, Warehouse, WarehouseTransaction

T = TypeVar('T')


class Repository(ABC, Generic[T]):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def create(self, obj: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(self, obj_id: int, obj: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int):
        raise NotImplementedError


class BaseRepository(Repository):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_by_id(self, id: int) -> Optional[T]:
        logger.debug(f'method get_by_id in repository')
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, obj: T) -> None:
        logger.debug(f'method create in repository')
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

    def update(self, obj_id: int, obj: T) -> None:
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
            logger.error(f'Object with id {obj_id} not found')
            raise
        except SQLAlchemyError as e:
            logger.error(f'Failed to update with id {obj_id} : {e}')
            self.db.rollback()
            raise

    def get_all(self) -> List[T]:
        logger.debug(f'method get_all in repository')
        return self.db.query(self.model).all()

    def delete(self, id: int) -> None:
        logger.debug(f'method delete in repository')
        model = self.get_by_id(id)
        self.db.delete(model)
        self.db.commit()


class CategoryRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Category)


class EmployeeRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Employee)


class OrderRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Order)


class ProductRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Product)

    def get_product_with_details(self):
        product_with_details = (
            self.db.query(Product)
            .join(Category, Category.id == Product.category_id)
            .join(Suppliers, Suppliers.id == Product.supplier_id)
            .options(joinedload(Product.category), joinedload(Product.suppliers))
        ).all()
        return product_with_details


class SuppliersRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Suppliers)


class WarehouseRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, Warehouse)


class WarehouseTransactionRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, WarehouseTransaction)
