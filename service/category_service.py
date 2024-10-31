from core.models import Category
from repository.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def create(self, category_name,description):
        category = Category(category_name = category_name,description=description)
        self.category_repository.add_category(category)

