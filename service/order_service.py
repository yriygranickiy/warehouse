from core.models import Order
from repository.order_repository import OrderRepository


class OrderService:

    def __init__(self,order_repository: OrderRepository):
        self.order_repository = order_repository

    def add_order(self, order: Order):
        self.order_repository.add(order)

    def get_all_orders(self):
        return self.order_repository.get_all()