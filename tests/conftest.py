from pathlib import Path

import pandas as pd
import pytest

from models.ticket import Ticket
from pipelines.triage import TriagePipeline


@pytest.fixture(scope = "module")
def trained_pipeline():
    DATA_PATH = Path(__file__).parent.parent /"data" / "mock_tickets.csv"
    df = pd.read_csv(DATA_PATH)
    mock_data = df[
    ["title", "description", "category", "urgency"]
].to_dict(orient="records")

    pipe = TriagePipeline(conf_threshold=0.6)
    pipe.train(mock_data)
    return pipe

@pytest.fixture
def sample_ticket():
    return Ticket(title="Payment failed", description= "Card declined during upgrade")