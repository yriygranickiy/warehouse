from core.models import Warehouse
from repository.wearhouse_repository import WarehouseRepository
from service.base_service import BaseService


class WarehouseService(BaseService[Warehouse]):
    def __init__(self, repository: WarehouseRepository):
        super().__init__(repository)


