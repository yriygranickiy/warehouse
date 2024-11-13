from sqlalchemy.orm import Session

from core.models import Product
from repository.base_repository import BaseRepository


class ProductRepository(BaseRepository[Product]):

    def __init__(self, session: Session):
        super().__init__(session, Product)
