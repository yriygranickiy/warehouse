from sqlalchemy.orm import Session

from core.models import Warehouse


class WarehouseRepository:
    def __init__(self, session:Session):
        self.session = session

    def add(self,warehouse:Warehouse):
        self.session.add(warehouse)
        self.session.commit()

    def get_all(self):
        self.session.query(Warehouse).all()