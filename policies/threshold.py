from policies.base import ConfidencePolicy


class ThresholdPolicy(ConfidencePolicy):
    def __init__(self, conf_threshold: float = 0.6):
        self.conf_threshold = conf_threshold

    def should_route_to_human(self, confidence: float, urgency: str) -> bool:
        return confidence < self.conf_threshold or urgency == "High"
