from contextlib import asynccontextmanager
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException
from loguru import logger
from pydantic import BaseModel

from models.ticket import Ticket
from pipelines.triage import TriagePipeline

DATA_PATH = Path(__file__).parent.parent / "data" / "mock_tickets.csv"

pipeline: TriagePipeline | None = None


class TicketInput(BaseModel):
    title: str
    description: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    global pipeline

    logger.info("Loading training data and initializing pipeline...")

    df = pd.read_csv(DATA_PATH)
    mock_data = df[["title", "description", "category", "urgency"]].to_dict(
        orient="records"
    )

    pipeline = TriagePipeline(conf_threshold=0.6)
    pipeline.train(mock_data)

    logger.info("Pipeline ready. Accepting tickets.")
    yield

    logger.info("Shutting down application...")


app = FastAPI(title="Ticket Triage Engine", lifespan=lifespan)


@app.post("/submit")
async def submit_ticket(ticket: TicketInput):
    if pipeline is None:
        raise HTTPException(status_code=503, detail="Pipeline not initialized")

    new_ticket = Ticket(title=ticket.title, description=ticket.description)
    result = pipeline.process(new_ticket)

    logger.info(f"Ticket {new_ticket.id[:8]} routed to {result['assigned_to']}")
    return result


@app.get("/health")
async def health_check():
    return {"status": "ok", "pipeline_ready": pipeline is not None}
