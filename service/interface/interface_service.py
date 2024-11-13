from typing import TypeVar, Protocol, Generic, List

T = TypeVar('T')
class IService(Protocol,Generic[T]):

    def get_by_id(self, id: int) -> T:
        ...

    def create(self, obj: T) -> T:
        ...

    def get_all(self)->List[T]:
        ...