from abc import ABC, abstractmethod
from models.ticket import Ticket

class Router(ABC):
    @abstractmethod
    def route(self, ticket: Ticket, prediction: dict) -> str:
        pass
    