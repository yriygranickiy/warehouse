from core.models import Suppliers
from repository.suppliers_repository import SuppliersRepository


class SuppliersService:
    def __init__(self, suppliers_repository: SuppliersRepository):
        self.suppliers_repository = suppliers_repository

    def create_suppliers(self, supp: Suppliers):
        self.suppliers_repository.add_supplier(supp)

    def get_all_suppliers(self):
        return self.suppliers_repository.get_all()

    def get_supplier_by_id(self, supplier_id):
        return self.suppliers_repository.get_suppliers_by_id(supplier_id)