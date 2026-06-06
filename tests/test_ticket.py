import pytest

from models.ticket import Ticket


def test_valid_ticket_creates_id_and_timestamp():
    t = Ticket(title="Test ticket", description="Checking auto-fields")
    assert t.id is not None
    assert t.created_at is not None
    assert t.category is None
    assert t.urgency is None


def test_title_too_short_raises_validation_error():
    with pytest.raises(Exception):
        Ticket(title="Hi", description="Too short")


def test_whitespace_stripped_automatically():
    t = Ticket(title="Login Issue", description="Cannot access")
    assert t.title == "Login Issue"
    assert t.description == "Cannot access"
