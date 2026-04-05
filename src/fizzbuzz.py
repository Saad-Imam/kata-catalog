import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_divisible_by_3(self):
        self.assertEqual(fizzbuzzHelper(3), 'Fizz')

    def test_divisible_by_5(self):
        self.assertEqual(fizzbuzzHelper(5), 'Buzz')

    def test_divisible_by_3_and_5(self):
        self.assertEqual(fizzbuzzHelper(15), 'FizzBuzz')

    def test_others(self):
        self.assertEqual(fizzbuzzHelper(1), '1')
        self.assertEqual(fizzbuzzHelper(2), '2')
        self.assertEqual(fizzbuzzHelper(4), '4')

def fizzbuzzHelper(n):
    return ""

if __name__ == '__main__':
    unittest.main()