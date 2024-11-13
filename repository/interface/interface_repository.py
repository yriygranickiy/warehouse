from typing import Protocol, Generic, TypeVar, Optional, Any, Dict, List

T = TypeVar('T')

class IRepository(Protocol, Generic[T]):

    def get_by_id(self, id: int) -> Optional[T]:
        ...

    def create(self, obj: T) -> T:
        ...

    def get_all(self) -> List[T]:
        ...
