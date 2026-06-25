from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import Boolean, DateTime, Float, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "triage.db"

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class TicketRecord(Base):
    __tablename__ = "tickets"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    category: Mapped[str | None] = mapped_column(String, nullable=True)
    urgency: Mapped[str | None] = mapped_column(String, nullable=True)

    confidence: Mapped[float] = mapped_column(Float, nullable=False)

    routed_to: Mapped[str] = mapped_column(String, nullable=False)

    sla_breach: Mapped[bool] = mapped_column(Boolean, default=False)

    processed_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
    )


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
