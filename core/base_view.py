from abc import abstractmethod
from datetime import time
from typing import TypeVar, Generic, Protocol

from core.base_repository import Repository
from core.base_service import Service

T = TypeVar('T')

class View(Protocol, Generic[T]):

    @abstractmethod
    def get_view_all(self):
        ...


class BaseView(View[T],Generic[T]):

    def __init__(self,service:Service[T]):
        self.service = service

    def get_view_all(self):
        print("Load list transaction...")
        for obj in self.service.get_all():
            print(obj)
            time.sleep(0.3)
        print("list load successfully!")



