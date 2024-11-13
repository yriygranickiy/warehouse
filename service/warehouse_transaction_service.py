from core.models import WarehouseTransaction
from repository.wearhouse_repository import WarehouseRepository
from service.base_service import BaseService


class WarehouseTransactionService(BaseService[WarehouseTransaction]):
    def __init__(self, repository: WarehouseRepository):
        super().__init__(repository)
