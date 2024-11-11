from sqlalchemy.orm import Session

from core.models import Suppliers


class SuppliersRepository:
    def __init__(self,session:Session):
        self.session = session

    def add_supplier(self,supplier):
        self.session.add(supplier)
        self.session.commit()

    def get_suppliers_by_id(self,supplier_id):
        return self.session.query(Suppliers).filter_by(id = supplier_id).all()

    def get_all(self):
        return self.session.query(Suppliers).all()

