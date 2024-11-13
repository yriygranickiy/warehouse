from sqlalchemy.orm import Session

from core.models import Suppliers
from repository.base_repository import BaseRepository


class SuppliersRepository(BaseRepository[Suppliers]):
    def __init__(self,session:Session):
        super().__init__(session,Suppliers)


