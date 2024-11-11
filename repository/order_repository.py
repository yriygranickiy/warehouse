from sqlalchemy.orm import Session

from core.models import Order


class OrderRepository:

    def __init__(self,session: Session):
        self.session = session

    def add(self,order: Order):
        self.session.add(order)
        self.session.commit()

    def get_all(self):
        return self.session.query(Order).all()

    def get_by_id(self,id):
        return self.session.query(Order).filter_by(id=id).first()