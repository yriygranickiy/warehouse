from core.models import Order
from repository.order_repository import OrderRepository
from service.base_service import BaseService


class OrderService(BaseService[Order]):
    def __init__(self, repository: OrderRepository):
        super().__init__(repository)
