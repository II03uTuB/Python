import unittest
from unittest.mock import patch
from helloworld.pz4 import Guesser

class TestGuesser(unittest.TestCase):
    def test_check(self):
        rnd = -100
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = -100
        should_ans = 0
        self.assertEqual(guesser.check(guess), should_ans)

        rnd = 0
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = 0
        should_ans = 0
        self.assertEqual(guesser.check(guess), should_ans)

        rnd = 26
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = 434535
        should_ans = 1
        self.assertEqual(guesser.check(guess), should_ans)

        rnd = 55555
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = 15
        should_ans = -1
        self.assertEqual(guesser.check(guess), should_ans)

        rnd = 124354
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = 124354
        should_ans = 0
        self.assertEqual(guesser.check(guess), should_ans)



    def test_play_all_wrong(self):
        rnd = 2
        user_input = ['10', '1', '3', '2']
        ret_check = [2, 1, -1, 0]
        countCalls = len(user_input)
        with patch('random.randint', return_value=rnd), \
             patch('builtins.input', side_effect=user_input), \
             patch('guesser.Guesser.check', side_effect=ret_check), \
             patch('builtins.print') as mock_print:
            guesser = Guesser()
            guesser.play()

            mock_print.assert_called_with('\nУспех! Верно угадано число {0}'.format(rnd))
            self.assertEqual(mock_print.call_count, countCalls)



    def test_play_error(self):
        rnd = 1
        user_input = ['qwargebt', '', '325a', 'qqqqqqqqqq']

        with patch('random.randint', return_value=rnd),\
             patch('builtins.input', side_effect=user_input):
            guesser = Guesser()
            with self.assertRaises(ValueError):
                guesser.play()

            with self.assertRaises(ValueError):
                guesser.play()

            with self.assertRaises(ValueError):
                guesser.play()
