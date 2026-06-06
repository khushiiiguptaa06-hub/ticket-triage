from abc import ABC, abstractmethod


class ConfidencePolicy(ABC):
    @abstractmethod
    def should_route_to_human(self, confidence: float, urgency: str) -> bool:
        pass
