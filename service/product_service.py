from core.models import Product
from repository.product_repository import ProductRepository


class ProductService:

    def __init__(self, repos:ProductRepository):
        self.repos = repos


    def create_product(self,product:Product):
        self.repos.add(product)

    def get_all_products(self):
        return self.repos.get_all()