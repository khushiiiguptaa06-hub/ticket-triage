#  AI Ticket Triage Engine

An AI-powered backend system that automatically classifies customer support tickets, predicts their category and urgency, routes them to the appropriate support team using confidence-aware routing, stores results in SQLite, and exposes REST APIs with FastAPI.

The project demonstrates modern backend development practices including Object-Oriented Programming (OOP), machine learning integration, REST API development, SQLAlchemy ORM, Docker containerization, automated testing, static type checking, and clean project architecture.

---

##  Features

*  Automatic ticket classification using Scikit-learn
*  Confidence-aware routing to support teams
*  Human review queue for low-confidence predictions
*  SQLite persistence using SQLAlchemy ORM
*  Metrics endpoint for processed tickets
*  FastAPI REST API
*  Interactive Swagger documentation
*  Unit testing with Pytest
*  Static type checking with MyPy
*  Code formatting with Ruff
*  Docker support

---

##  Architecture

```text
                 Client
                    │
                    ▼
              FastAPI REST API
                    │
                    ▼
             Ticket Validation
                    │
                    ▼
        Scikit-Learn Classifier
                    │
                    ▼
        Confidence Threshold Policy
              │               │
              ▼               ▼
      Support Team      Human Review
              │
              ▼
      SQLAlchemy + SQLite
              │
              ▼
        Metrics & Analytics
```

---

##  Tech Stack

| Category         | Technologies |
| ---------------- | ------------ |
| Language         | Python 3.13  |
| API              | FastAPI      |
| Machine Learning | Scikit-learn |
| Data Processing  | Pandas       |
| Validation       | Pydantic     |
| Database         | SQLite       |
| ORM              | SQLAlchemy   |
| Logging          | Loguru       |
| Testing          | Pytest       |
| Static Analysis  | MyPy         |
| Formatting       | Ruff         |
| Containerization | Docker       |

---

##  Project Structure

```text
ticket-triage/
│
├── api/
├── classifiers/
├── db/
├── data/
├── models/
├── observers/
├── pipelines/
├── policies/
├── routers/
├── tests/
│
├── Dockerfile
├── .dockerignore
├── pyproject.toml
├── README.md
├── run_classifier.py
├── run_phase2.py
└── run_pipeline.py
```

---

##  API Endpoints

### Submit Ticket

```
POST /submit
```

Example Request

```json
{
  "title": "Payment failed",
  "description": "Card declined during subscription upgrade."
}
```

Example Response

```json
{
  "ticket_id": "...",
  "category": "Account",
  "urgency": "High",
  "confidence": 0.82,
  "assigned_to": "account-team"
}
```

---

### Health Check

```
GET /health
```

Response

```json
{
  "status": "ok",
  "pipeline_ready": true
}
```

---

### Metrics

```
GET /metrics
```

Returns

* Total processed tickets
* Human review count
* Average confidence
* SLA breach count

---

##  Running Locally

Clone the repository

```bash
git clone https://github.com/<your-username>/ticket-triage.git
cd ticket-triage
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -e .
```

Run the API

```bash
uvicorn api.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

##  Running with Docker

Build the image

```bash
docker build -t ticket-triage .
```

Run the container

```bash
docker run -p 8000:8000 ticket-triage
```

Open

```
http://localhost:8000/docs
```

---

##  Running Tests

```bash
pytest
```

---

##  Code Quality

Run Ruff

```bash
ruff format .
```

Run MyPy

```bash
python -m mypy .
```

---

##  Future Improvements

* JWT Authentication
* PostgreSQL support
* Redis caching
* Background task queue (Celery)
* CI/CD with GitHub Actions
* Cloud deployment
* Model retraining pipeline
* Dashboard for analytics

---


##  Author

**Khushi Gupta**

B.Tech Computer Science Engineering

Aspiring AI/ML & Backend Developer

---

##  License

This project is intended for educational and portfolio purposes.
