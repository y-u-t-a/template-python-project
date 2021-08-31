from unittest.mock import ANY

from src.main import echo

def test_echo():
    assert echo(ANY) == ANY