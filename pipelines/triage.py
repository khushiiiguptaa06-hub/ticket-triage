# pipelines/triage.py
from datetime import datetime, timezone

from classifiers.sklearn_cls import SklearnClassifier
from models.ticket import Ticket
from observers.metrics import MetricsCollector
from policies.threshold import ThresholdPolicy
from routers.confidence_aware import ConfidenceAwareRouter
from routers.rule_based import RuleBasedRouter


class TriagePipeline:
    def __init__(self, conf_threshold: float = 0.6):
        self.classifier = SklearnClassifier()
        self.rule_router = RuleBasedRouter()
        self.conf_policy = ThresholdPolicy(conf_threshold=conf_threshold)
        self.router = ConfidenceAwareRouter(self.rule_router, self.conf_policy)
        self.metrics = MetricsCollector()

    def train(self, mock_data: list[dict]) -> None:
        self.classifier.train(mock_data)

    def process(self, ticket: Ticket) -> dict:
        processed_at = datetime.now(timezone.utc)
        prediction = self.classifier.predict(ticket)
        assigned_team = self.router.route(ticket, prediction)
        
        self.metrics.record(
            ticket.id, prediction["category"], prediction["urgency"],
            prediction["confidence"], assigned_team, processed_at
        )

        return {
            "ticket_id": ticket.id,
            "category": prediction["category"],
            "urgency": prediction["urgency"],
            "confidence": prediction["confidence"],
            "assigned_to": assigned_team,
            "metrics_summary": self.metrics.summary()
        }