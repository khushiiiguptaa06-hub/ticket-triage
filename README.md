<<<<<<< HEAD
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
=======
# AI Ticket Triage Engine

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)

An AI-powered backend system that automatically classifies customer support tickets, predicts their category and urgency, routes them to the appropriate support team using confidence-aware routing, stores processed tickets in SQLite, and exposes REST APIs using FastAPI.

The project demonstrates modern backend engineering practices including machine learning integration, object-oriented design, REST API development, SQLAlchemy ORM, Docker containerization, automated testing, and static type checking. Its modular architecture separates machine learning, routing, persistence, and API layers, making the system easy to maintain and extend.

---

## Live Demo

**Deployment in progress.** The live API URL will be added after deployment on Render.

---

## Features

* Automatic ticket classification using Scikit-learn
* Confidence-aware routing based on prediction confidence
* Human review queue for low-confidence predictions
* SQLite persistence using SQLAlchemy ORM
* Metrics endpoint for processed tickets
* REST API built with FastAPI
* Interactive Swagger API documentation
* Dockerized application
* Unit testing with Pytest
* Static type checking with MyPy
* Code formatting with Ruff

---

## Design Patterns Used

* Strategy Pattern
* Observer Pattern
* Dependency Injection
* Modular Pipeline Architecture

---

## Architecture

```text
                  Client
                     │
                     ▼
              FastAPI REST API
                     │
                     ▼
             Request Validation
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

## Tech Stack

| Category         | Technology   |
| ---------------- | ------------ |
| Language         | Python       |
| API Framework    | FastAPI      |
| Machine Learning | Scikit-learn |
| Data Processing  | Pandas       |
| Validation       | Pydantic     |
| Database         | SQLite       |
| ORM              | SQLAlchemy   |
| Logging          | Loguru       |
| Testing          | Pytest       |
| Static Analysis  | MyPy         |
| Code Formatter   | Ruff         |
| Containerization | Docker       |

---

## Project Structure

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

## API Endpoints

| Method | Endpoint   | Description                                |
| ------ | ---------- | ------------------------------------------ |
| POST   | `/submit`  | Submit a support ticket for classification |
| GET    | `/health`  | Check application health                   |
| GET    | `/metrics` | View ticket processing metrics             |

### Example Request

```json
{
  "title": "Payment failed",
  "description": "Card declined during subscription upgrade."
}
```

### Example Response

```json
{
  "ticket_id": "f4a4b1...",
  "category": "Account",
  "urgency": "High",
  "confidence": 0.82,
  "assigned_to": "account-team"
}
```

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/khushiiiguptaa06-hub/ticket-triage.git
cd ticket-triage
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -e .
```

### Run the Application

```bash
uvicorn api.main:app --reload
```

Open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running with Docker

Build the Docker image:

```bash
docker build -t ticket-triage .
```

Run the container:

```bash
docker run -p 8000:8000 ticket-triage
```

Access the API:

```text
http://localhost:8000/docs
```

---

## Testing

Run the test suite:

```bash
pytest
```

---

## Code Quality

Format the code:

```bash
ruff format .
```

Run static type checking:

```bash
python -m mypy .
```

---

## Screenshots

The following screenshots will be added after deployment:

* Swagger API Documentation
* Ticket Submission Example
* Metrics Endpoint
* Docker Container Running

---

## Future Improvements

* JWT Authentication
* PostgreSQL support
* Redis caching
* Background task processing with Celery
* CI/CD using GitHub Actions
* Cloud deployment
* Model retraining pipeline
* Analytics dashboard

---

## Author

**Khushi Gupta**

B.Tech Computer Science Engineering

Aspiring AI/ML & Backend Developer

---

## License

This project is intended for educational and portfolio purposes.
>>>>>>> 1c9c269 (docs: improve README and add Docker support)
