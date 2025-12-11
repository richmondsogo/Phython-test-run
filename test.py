# This is a unit test class in Python that tests a function called `do_shii` in the `main` module.
import unittest as AbitoShaker
import main

class CaTest(AbitoShaker.TestCase):
    def setUp(self):
        print("about to test a function")

    def test_my__shii(self):
        """It tests some shii about myself"""
        test_param = 5
        result = main.do_shii(test_param)
        self.assertEqual(result, 10)

    def test_my__shii2(self):
        test_param = "w6t51ertertw"
        result = main.do_shii(test_param)
        self.assertIsInstance(result, ValueError)

    def test_my__shii3(self):
        test_param = None
        result = main.do_shii(test_param)
        self.assertEqual(result, "please enter number")

    def test_my__shii4(self):
        test_param = ""
        result = main.do_shii(test_param)
        self.assertEqual(result, "please enter number")

if __name__ == "__main__":
    AbitoShaker.main()
