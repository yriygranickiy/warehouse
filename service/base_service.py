from typing import Generic, List

from repository.interface.interface_repository import IRepository
from service.interface.interface_service import IService, T


class BaseService(IService[T], Generic[T]):
    def __init__(self, repository: IRepository[T]):
        self.repository = repository

    def get_by_id(self, id: int) -> T:
        return self.repository.get_by_id(id)

    def create(self, data: T) -> T:
        self.repository.create(data)

    def get_all(self) -> List[T]:
        return self.repository.get_all()
