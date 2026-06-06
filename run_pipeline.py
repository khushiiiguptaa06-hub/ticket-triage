from pathlib import Path

import pandas as pd

from models.ticket import Ticket
from pipelines.triage import TriagePipeline

DATA_PATH = Path(__file__).parent / "data" / "mock_tickets.csv"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    mock_data = df[["title", "description", "category", "urgency"]].to_dict(
        orient="records"
    )

    pipeline = TriagePipeline()
    pipeline.train(mock_data)

    print("Pipeline trained")

    new_ticket = Ticket(
        title="Payment failed",
        description="Card declined during subscription upgrade",
    )

    result = pipeline.process(new_ticket)

    print(f"Triage Result:\n{result}")


if __name__ == "__main__":
    main()
