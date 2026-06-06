from typing import Any

from models.ticket import Ticket
from policies.base import ConfidencePolicy
from routers.base import Router


class ConfidenceAwareRouter(Router):
    def __init__(
        self,
        rule_router: Router,
        policy: ConfidencePolicy,
    ) -> None:
        self.rule_router = rule_router
        self.policy = policy

    def route(
        self,
        ticket: Ticket,
        prediction: dict[str, Any],
    ) -> str:
        if self.policy.should_route_to_human(
            prediction["confidence"],
            prediction["urgency"],
        ):
            return "human-review"

        return self.rule_router.route(ticket, prediction)