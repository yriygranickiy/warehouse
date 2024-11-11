from sqlalchemy.orm import Session

from core.models import WarehouseTransaction


class WarehouseTransactionRepository:
    def __init__(self,session:Session):
        self.session = session

    def add(self,warehouse_transaction:WarehouseTransaction):
        self.session.add(warehouse_transaction)
        self.session.commit()

    def get_all(self):
        return self.session.query(WarehouseTransaction).all()

    def get_by_id(self,id):
        return self.session.query(WarehouseTransaction).filter_by(id=id).first()