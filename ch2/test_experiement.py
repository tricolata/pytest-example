import cards
import pytest

# def test_no_path_fail():
#     cards.CardsDB()

def test_no_path_raises():
    with pytest.raises(TypeError):
        cards.CardsDB()