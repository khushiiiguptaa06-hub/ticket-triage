from pathlib import Path

import pandas as pd

from classifiers.sklearn_cls import SklearnClassifier
from models.ticket import Ticket

DATA_PATH = Path(__file__).parent / "data" / "mock_tickets.csv"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    mock_tickets = df[["title", "description", "category", "urgency"]].to_dict(
        orient="records"
    )

    cls = SklearnClassifier()
    cls.train(mock_tickets)

    print("Trained on mock data")

    test_tickets = Ticket(
        title="Billing issue",
        description="Was charged twice this month",
    )

    result = cls.predict(test_tickets)

    print(f"Prediction: {result}")


if __name__ == "__main__":
    main()
