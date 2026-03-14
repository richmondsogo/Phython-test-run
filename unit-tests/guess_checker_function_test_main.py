import unittest
import main

# The TestGuessChecker class contains a unit test for checking if a guess is correct.
class TestGuessChecker(unittest.TestCase):
    def test_correct_guess(self):
        answer = 5
        guess = 5
        result = main.guess_checker(guess, answer)
        self.assertTrue(result)

    def test_wrong_guess(self):
        answer = 5
        guess = 6
        result = main.guess_checker(guess, answer)
        self.assertFalse(result)

    def test_wrong_value(self):
        answer = 6
        guess = 44
        result = main.guess_checker(guess, answer)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
