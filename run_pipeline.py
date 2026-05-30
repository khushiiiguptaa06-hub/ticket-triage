from models.ticket import Ticket
from pipelines.triage import TriagePipeline
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "mock_tickets.csv"

def main():
   
    df = pd.read_csv(DATA_PATH)
    mock_data = df[["title", "description", "category", "urgency"]].to_dict(orient="records")
    
    pipeline = TriagePipeline()
    pipeline.train(mock_data)
    print(" Pipeline trained")

    
    new_ticket = Ticket(title="Payment failed", description="Card declined during subscription upgrade")
    result = pipeline.process(new_ticket)
    print(f" Triage Result:\n{result}")

if __name__ == "__main__":
    main()