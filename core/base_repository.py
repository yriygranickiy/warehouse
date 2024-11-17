from abc import abstractmethod
from typing import Type, Optional, List, TypeVar, Protocol, Generic


from sqlalchemy.orm import Session

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
    def get_all(self) -> List[T]:
        ...


class BaseRepository(Repository[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_by_id(self, id: int) -> Optional[T]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, obj: T) -> T:

        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

    def get_all(self) -> List[T]:
        return self.db.query(self.model).all()

class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: Session):
        super().__init__(session,Category)

class EmployeeRepository(BaseRepository[Employee]):
    def __init__(self, session: Session):

        super().__init__(session,Employee)

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

