from pathlib import Path

import pandas as pd

from models.ticket import Ticket
from pipelines.triage import TriagePipeline

DATA_PATH = Path(__file__).parent / "data" / "mock_tickets.csv"


def main() -> None:
    
    df = pd.read_csv(DATA_PATH)

    mock_data = df[
        ["title", "description", "category", "urgency"]
    ].to_dict(orient="records")

    # Create and train pipeline
    pipeline = TriagePipeline(conf_threshold=0.6)
    pipeline.train(mock_data)

    # Test ticket 1 - likely billing
    t1 = Ticket(
        title="Payment failed",
        description="Card declined during subscription upgrade",
    )

    result1 = pipeline.process(t1)

    print("\n🎫 Ticket 1")
    print(result1)

    # Test ticket 2 - gibberish / low confidence
    t2 = Ticket(
        title="asdf",
        description="zxcv qwer random noise no context",
    )

    result2 = pipeline.process(t2)

    print("\n🎫 Ticket 2")
    print(result2)

    # Test ticket 3 - urgent access issue
    t3 = Ticket(
        title="Urgent login issue",
        description="Can't access critical systems, blocking production",
    )

    result3 = pipeline.process(t3)

    print("\n🎫 Ticket 3")
    print(result3)

    print("\n Metrics Summary")
    print(pipeline.metrics.summary())


if __name__ == "__main__":
    main()