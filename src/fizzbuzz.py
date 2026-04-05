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
        
        
    def test_divbyzero(self):
        with self.assertRaises(ZeroDivisionError):
            fizzbuzzHelper(0)

def fizzbuzzHelper(n):
    if n == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def fizzbuzz():
    for i in range(1, 101):
        print(fizzbuzzHelper(i))

if __name__ == '__main__':
    #unittest.main()
    #fizzbuzz()
    fizzbuzzHelper(-3)
