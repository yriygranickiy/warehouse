from core.models import Suppliers
from repository.suppliers_repository import SuppliersRepository


class SuppliersService:
    def __init__(self, suppliers_repository: SuppliersRepository):
        self.suppliers_repository = suppliers_repository

    def create_suppliers(self,name_supplier,contact_person,phone,email,address):

        new_supplier = Suppliers(
            supplier_name = name_supplier,
            contact_person = contact_person,
            phone = phone,
            email = email,
            address=address)

        self.suppliers_repository.add_supplier(new_supplier)

    def get_all_suppliers(self):
        return self.suppliers_repository.get_all()
