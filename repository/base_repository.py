from typing import Type, Optional, List

from sqlalchemy.orm import Session

from repository.interface.interface_repository import IRepository, T


class BaseRepository(IRepository[T]):
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