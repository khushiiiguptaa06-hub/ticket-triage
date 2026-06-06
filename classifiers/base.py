from abc import ABC, abstractmethod

from models.ticket import Ticket


class Classifier(ABC):
    @abstractmethod
    def train(self, tickets: list[dict[str, str]]) -> None:
        pass

    @abstractmethod
    def predict(self, ticket: Ticket) -> dict[str, object]:
        pass
