from sqlalchemy.orm import Session

from core.models import Order
from repository.base_repository import BaseRepository


class OrderRepository(BaseRepository[Order]):

    def __init__(self, session: Session):
        super().__init__(session, Order)
