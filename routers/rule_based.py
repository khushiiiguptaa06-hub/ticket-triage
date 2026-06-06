from typing import Any

from models.ticket import Ticket
from routers.base import Router


class RuleBasedRouter(Router):
    def route(self, ticket: Ticket, prediction: dict[str, Any]) -> str:
        category = prediction.get("category")

        if category == "Billing":
            return "finance-team"

        if category in ("Tech", "Bug"):
            return "engineering-team"

        if category == "Account":
            return "support-team"

        return "general-queue"
