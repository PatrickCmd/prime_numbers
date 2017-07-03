import unittest
from primes import Primes

class primeTests(unittest.TestCase):

    def setUp(self):
        self.prime = Primes()

    def prime_returns_error_if_not_number(self):
        self.assertRaises(ValueError, self.prime.primeNumbers, 'Value is not number')
    
    def prime_number_less_than_one(self):
        number = self.prime.primeNumbers(-1)
        self.assertEqual(-1, number, 'Numbers less than 1 are not prime numbers')

    def prime_is_number_prime_or_not(self):
        number = self.prime.primeNumbers(6)
        result = number % 2
        self.assertEqual(0, result, 'Number is not prime')


if __name__ == '__main__':
    unittest.main()