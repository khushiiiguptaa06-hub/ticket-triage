import random
from datetime import datetime
from typing import Any


class MetricsCollector:
    def __init__(self) -> None:
        self.logs: list[dict[str, Any]] = []

    def record(
        self,
        ticket_id: str,
        category: str,
        urgency: str,
        confidence: float,
        routed_to: str,
        processed_at: datetime,
    ) -> None:
        # High-priority tickets have stricter SLA
        sla_limit = 15 if urgency == "High" else 30

        # Simulate resolution time (5–50 min)
        simulated_resolution_min = random.randint(5, 50)

        sla_breach = simulated_resolution_min > sla_limit

        self.logs.append(
            {
                "ticket_id": ticket_id,
                "category": category,
                "urgency": urgency,
                "confidence": confidence,
                "routed_to": routed_to,
                "sla_breach": sla_breach,
                "simulated_resolution_min": simulated_resolution_min,
                "processed_at": processed_at.isoformat(),
            }
        )

    def summary(self) -> dict[str, Any]:
        if not self.logs:
            return {
                "total_processed": 0,
                "human_review_ratio": 0,
                "avg_confidence": 0,
                "sla_breach_rate": 0,
            }

        human_reviews = sum(
            1 for log in self.logs if log["routed_to"] == "human-review"
        )

        breaches = sum(1 for log in self.logs if log["sla_breach"])

        avg_confidence = sum(log["confidence"] for log in self.logs) / len(self.logs)

        return {
            "total_processed": len(self.logs),
            "human_review_ratio": round(
                human_reviews / len(self.logs),
                2,
            ),
            "avg_confidence": round(
                avg_confidence,
                3,
            ),
            "sla_breach_rate": round(
                breaches / len(self.logs),
                2,
            ),
        }
