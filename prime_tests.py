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
    

if __name__ == '__main__':
    unittest.main()