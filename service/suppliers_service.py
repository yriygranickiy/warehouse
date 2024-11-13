from core.models import Suppliers
from repository.suppliers_repository import SuppliersRepository
from service.base_service import BaseService


class SuppliersService(BaseService[Suppliers]):
    def __init__(self, repository: SuppliersRepository):
        super().__init__(repository)

