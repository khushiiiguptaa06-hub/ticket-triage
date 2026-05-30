from models.ticket import Ticket
from classifiers.sklearn_cls import SklearnClassifier
from routers.rule_based import RuleBasedRouter

class TriagePipeline:
    def __init__(self):
        self.classifier = SklearnClassifier()
        self.router = RuleBasedRouter()

    def train(self, mock_data: list[dict]) -> None:
        """One-time training step."""
        self.classifier.train(mock_data)

    def process(self, ticket: Ticket) -> dict:
        """Full triage flow: classify → route → return result."""
        prediction = self.classifier.predict(ticket)
        assigned_team = self.router.route(ticket, prediction)
        
        return {
            "ticket_id": ticket.id,
            "category": prediction["category"],
            "urgency": prediction["urgency"],
            "confidence": prediction["confidence"],
            "assigned_to": assigned_team
        }