from abc import ABC, abstractmethod
from typing import List, Dict
from models.ticket import Ticket

class Classifier(ABC):
    @abstractmethod
    def train(self, tickets: List[Dict[str, str]]) -> None:
        pass
    
    @abstractmethod
    def predict(self, ticket: Ticket) -> Dict[str, object]:
        pass
