from unittest import TestCase
from unittest.mock import ANY

from src.main import echo

class TestMain(TestCase):
    def test_echo(self):
        self.assertEqual(echo(ANY), ANY)