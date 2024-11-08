from core.models import Warehouse
from repository.wearhouse_repository import WarehouseRepository


class WarehouseService:
    def __init__(self,repository:WarehouseRepository):
        self.repository = repository

    def add(self,warehouse:Warehouse):
        self.repository.add(warehouse)

    def get_all(self):
        return self.repository.get_all()
