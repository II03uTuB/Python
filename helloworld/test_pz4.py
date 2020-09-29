import unittest
from unittest.mock import patch
from helloworld.pz4 import Guesser

class TestGuesser(unittest.TestCase):
    def test_check(self):
        rnd = 15
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = 15
        should_ans = 0
        self.assertEqual(guesser.check(guess), should_ans)
