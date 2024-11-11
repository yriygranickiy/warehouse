from core.models import Product
from repository.product_repository import ProductRepository


class ProductService:

    def __init__(self, repository:ProductRepository):
        self.repository = repository


    def create_product(self,product:Product):
        self.repository.add(product)

    def get_all_products(self):
        return self.repository.get_all()

    def get_product_by_id(self, product_id):
        return self.repository.get_by_id(product_id)