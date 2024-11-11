from sqlalchemy.orm import Session

from core.models import Product


class ProductRepository:

    def __init__(self, session:Session):
        self.session = session

    def add(self, product:Product):
        self.session.add(product)
        self.session.commit()

    def get_all(self):
        return self.session.query(Product).all()

    def get_by_id(self, id):
        return self.session.query(Product).filter_by(id=id).first()