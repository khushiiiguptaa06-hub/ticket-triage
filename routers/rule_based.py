from models.ticket import Ticket
from routers.base import Router


class RuleBasedRouter(Router):
    def route(self, ticket: Ticket, prediction: dict) -> str:
        category = prediction.get("category")

        if category == "Billing":
            return "finance-team"
        elif category in("Tech", "Bug"):
            return "engineering-team"
        elif category =="Account":
            return "support-team"
        else:
            return "general-queue"
        

