from sqlalchemy.orm import Session

from core.models import WarehouseTransaction
from repository.base_repository import BaseRepository


class WarehouseTransactionRepository(BaseRepository[WarehouseTransaction]):
    def __init__(self,session:Session):
        super().__init__(session,WarehouseTransaction)
