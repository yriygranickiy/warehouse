from core.models import Category
from repository.category_repository import CategoryRepository
from service.base_service import BaseService


class CategoryService(BaseService[Category]):
    def __init__(self, repository: CategoryRepository):
        super().__init__(repository)
