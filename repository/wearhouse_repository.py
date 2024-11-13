from sqlalchemy.orm import Session

from core.models import Warehouse
from repository.base_repository import BaseRepository


class WarehouseRepository(BaseRepository[Warehouse]):
    def __init__(self, session:Session):
        super().__init__(session,Warehouse)
