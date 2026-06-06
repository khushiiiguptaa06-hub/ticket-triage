import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

from classifiers.base import Classifier
from models.ticket import Category, Ticket, Urgency


class SklearnClassifier(Classifier):
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english", max_features=500)
        self.model = MultiOutputClassifier(LogisticRegression())
        self.categories = [c.value for c in Category]
        self.urgencies = [u.value for u in Urgency]

    def train(self, tickets: list[dict[str, str]]) -> None:
        df = pd.DataFrame(tickets)
        texts = df["title"] + " " + df["description"]
        X = self.vectorizer.fit_transform(texts)
        y = np.column_stack([df["category"], df["urgency"]])
        self.model.fit(X, y)

    def predict(self, ticket: Ticket) -> dict[str, object]:
        text = f"{ticket.title} {ticket.description}"
        X = self.vectorizer.transform([text])
        preds = self.model.predict(X)[0]
        probs = self.model.predict_proba(X)

        confidence = float(np.mean([np.max(p) for p in probs]))
        return {
            "category": preds[0],
            "urgency": preds[1],
            "confidence": round(confidence, 3),
        }
