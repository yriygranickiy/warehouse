from sqlalchemy.orm import Session

from core.models import Category
from repository.base_repository import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: Session):
        super().__init__(session,Category)



