from core.models import WarehouseTransaction
from repository.wearhouse_repository import WarehouseRepository


class WarehouseTransactionService:
    def __init__(self,repository:WarehouseRepository):
        self.repository = repository

    def add(self,warehouse_transaction:WarehouseTransaction):
        self.repository.add(warehouse_transaction)

    def get_all(self):
        return self.repository.get_all()

    def get_transaction_by_id(self,transaction_id):
        return self.repository.get_by_id(transaction_id)