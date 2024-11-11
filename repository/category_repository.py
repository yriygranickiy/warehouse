from sqlalchemy.orm import Session

from core.models import Category


class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_category(self, category: Category):
        self.session.add(category)
        self.session.commit()

    def get_all_categories(self):
        return self.session.query(Category).all()

    def get_by_id(self, category_id):
        return self.session.query(Category).filter_by(id=category_id).first()

    def delete_category(self, category_id):
        self.session.delete(category_id)
        self.session.commit()


