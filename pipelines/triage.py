from datetime import datetime, timezone
from typing import Any, cast

from classifiers.sklearn_cls import SklearnClassifier
from models.ticket import Ticket
from observers.metrics import MetricsCollector
from policies.threshold import ThresholdPolicy
from routers.confidence_aware import ConfidenceAwareRouter
from routers.rule_based import RuleBasedRouter


class TriagePipeline:
    def __init__(self, conf_threshold: float = 0.6) -> None:
        self.classifier = SklearnClassifier()
        self.rule_router = RuleBasedRouter()
        self.conf_policy = ThresholdPolicy(conf_threshold=conf_threshold)

        self.router = ConfidenceAwareRouter(
            self.rule_router,
            self.conf_policy,
        )

        self.metrics = MetricsCollector()

    def train(
        self,
        mock_data: list[dict[str, str]],
    ) -> None:
        self.classifier.train(mock_data)

    def process(
        self,
        ticket: Ticket,
    ) -> dict[str, Any]:
        processed_at = datetime.now(timezone.utc)

        prediction = self.classifier.predict(ticket)

        assigned_team = self.router.route(
            ticket,
            prediction,
        )

        category = str(prediction["category"])
        urgency = str(prediction["urgency"])
        confidence = cast(float, prediction["confidence"])

        self.metrics.record(
            ticket.id,
            category,
            urgency,
            confidence,
            assigned_team,
            processed_at,
        )

        return {
            "ticket_id": ticket.id,
            "category": category,
            "urgency": urgency,
            "confidence": confidence,
            "assigned_to": assigned_team,
            "metrics_summary": self.metrics.summary(),
        }