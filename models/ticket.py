import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, ValidationError, field_validator


class Category(str, Enum):
    BILLING = "Billing"
    TECH = "Tech"
    ACCOUNT = "Account"
    BUG = "Bug"
    FEATURE = "Feature"

class Urgency(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Ticket(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(...,min_length=3, max_length=150) 
    description: str = Field(...,min_length=10, max_length=2000)
    category: Category | None = None
    urgency: Urgency | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    @field_validator("title", "description",mode="before")
    @classmethod
    def strip_whitespace(cls, v: Any) -> Any:
        """Sanitize input before Pydantic tries to coerce it."""
        if isinstance(v,str):
            return v.strip()
        return v
    
if __name__ == "__main__":
    t1 = Ticket(
    title="Login broken",
    description="Can't access dashboard after 2FA reset",)
    
    print(f"Valid: {t1.title} | ID: {t1.id[:8]}... | Created: {t1.created_at}")
    t2 = Ticket(title="Overcharged! ", description=" Charged twice, need refund ASAP")
    print(f"🧹 Cleaned: title='{t2.title}' | desc='{t2.description}'")

    try:
        Ticket(title = "Hi",description="This will fail because title is too short")
    except ValidationError as e:
        print(f"Blocked as expected: {e}")    