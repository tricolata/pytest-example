from cards import Card
import pytest

def test_field_access():
    c = Card("some summary", "some owner","todo", 123)
    assert c.summary == "some summary"
    assert c.owner == "some owner"
    assert c.state == "todo"
    assert c.id == 123

def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None

def test_equality():
    c1 = Card(summary="some", owner="some", id=123)
    c2 = Card(summary="some", owner="some", id=123)
    assert c1 == c2

def test_equality_diff_id():
    c1 = Card("some", "some", "todo",123)
    c2 = Card("some", "some", "todo",456)
    assert c1 == c2

def test_inequality():
    c1 = Card("some", "some","todo" , 123)
    c2 = Card("other", "other","done", 123)
    if c1 != c2:
        pytest.fail("They don't match")

def test_from_dict():
    c1 = Card("some", "Brian", "todo", 123)
    c2_dict = {
        "summary" : "some",
        "owner" : "Brian",
        "state" : "todo",
        "id" : 123
    }

    c2 = Card.from_dict(c2_dict)
    assert c1 == c2

def test_to_dict():
    c1 = Card("some", "Brian", "todo", 123)
    c2 = c1.to_dict()
    c2_expected = {
        "summary" : "some",
        "owner" : "Brian",
        "state" : "todo",
        "id" : 123
    }
    assert c2 == c2_expected


if __name__ == "__main__":
    test_to_dict()