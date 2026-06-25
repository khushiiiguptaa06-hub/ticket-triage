from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

import pandas as pd
from fastapi import FastAPI, HTTPException
from loguru import logger
from pydantic import BaseModel
from sqlalchemy import func

from db.models import SessionLocal, TicketRecord, init_db
from models.ticket import Ticket
from pipelines.triage import TriagePipeline

DATA_PATH = Path(__file__).parent.parent / "data" / "mock_tickets.csv"

pipeline: TriagePipeline | None = None


class TicketInput(BaseModel):
    title: str
    description: str


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    global pipeline

    logger.info("Loading training data and initializing pipeline...")
    init_db()

    df = pd.read_csv(DATA_PATH)

    mock_data = df[["title", "description", "category", "urgency"]].to_dict(
        orient="records"
    )

    pipeline = TriagePipeline(conf_threshold=0.6)
    pipeline.train(mock_data)

    logger.info("Pipeline ready. Accepting tickets.")

    yield

    logger.info("Shutting down application...")


app = FastAPI(
    title="Ticket Triage Engine",
    lifespan=lifespan,
)


@app.post("/submit")
async def submit_ticket(
    ticket: TicketInput,
) -> dict[str, Any]:
    if pipeline is None:
        raise HTTPException(
            status_code=503,
            detail="Pipeline not initialized",
        )

    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
    )

    result = pipeline.process(new_ticket)

    logger.info(f"Ticket {new_ticket.id[:8]} routed to {result['assigned_to']}")

    return result


@app.get("/health")
async def health_check() -> dict[str, Any]:
    return {
        "status": "ok",
        "pipeline_ready": pipeline is not None,
    }


@app.get("/metrics")
async def get_metrics() -> dict[str, Any]:
    session = SessionLocal()

    try:
        total = session.query(TicketRecord).count()

        if total == 0:
            return {
                "message": "No tickets processed yet",
            }

        human_reviews = (
            session.query(TicketRecord).filter_by(routed_to="human-review").count()
        )

        avg_conf = session.query(func.avg(TicketRecord.confidence)).scalar() or 0.0

        sla_breaches = session.query(TicketRecord).filter_by(sla_breach=True).count()

        return {
            "total_processed": total,
            "human_review_count": human_reviews,
            "human_review_ratio": round(
                human_reviews / total,
                2,
            ),
            "avg_confidence": round(
                float(avg_conf),
                3,
            ),
            "sla_breach_count": sla_breaches,
        }

    finally:
        session.close()
