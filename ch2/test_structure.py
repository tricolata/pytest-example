from cards import Card

def test_to_dict():
    # GIVEN a cards object with known contents
    c1 = Card("something", "brian", "todo", 123)

    # WHEN we call to_dict() on the object
    c2 = c1.to_dict()

    # THEN the result will be a dictionary with known content
    c2_expected = {
        "summary": "something", 
        "owner": "brian", 
        "state": "todo",
        "id": 123
    }

    assert c2 == c2_expected

    # GIVEN/ARRANGE - starting state. Where you prepare for the main action
    # WHEN/ACT - some action is performed. focus of the test.
    # THEN/ASSERT - Some expected result should happen. Verify expected action happened.