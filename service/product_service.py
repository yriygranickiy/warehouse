from core.models import Product
from repository.product_repository import ProductRepository
from service.base_service import BaseService


class ProductService(BaseService[Product]):

    def __init__(self, repository: ProductRepository):
        super().__init__(repository)
