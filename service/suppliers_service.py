from core.models import Suppliers
from repository.suppliers_repository import SuppliersRepository


class SuppliersService:
    def __init__(self, suppliers_repository: SuppliersRepository):
        self.suppliers_repository = suppliers_repository

    def create_suppliers(self, supp: Suppliers):
        self.suppliers_repository.add_supplier(supp)

    def get_all_suppliers(self):
        return self.suppliers_repository.get_all()
