from pathlib import Path

import pandas as pd
import pytest

from models.ticket import Ticket
from pipelines.triage import TriagePipeline


@pytest.fixture(scope="module")
def trained_pipeline() -> TriagePipeline:
    data_path = Path(__file__).parent.parent / "data" / "mock_tickets.csv"

    df = pd.read_csv(data_path)

    mock_data = df[["title", "description", "category", "urgency"]].to_dict(
        orient="records"
    )

    pipe = TriagePipeline(conf_threshold=0.6)
    pipe.train(mock_data)

    return pipe


@pytest.fixture
def sample_ticket() -> Ticket:
    return Ticket(
        title="Payment failed",
        description="Card declined during upgrade",
    )
