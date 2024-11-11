from core.models import Category
from repository.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def create(self, category: Category):
        self.category_repository.add_category(category)


    def get_all(self):
        return self.category_repository.get_all_categories()

    def get_category_by_id(self,category_id ):
        return self.category_repository.get_by_id(category_id)