class Primes(object):

    def primeNumbers(self, n):
        '''Display prime numbers from 0 to n'''

        # value must be a number and an integer
        if not isinstance(n, int):
            raise ValueError('Value must be an integer number. Try again!')

        print('Prime numbers from 0 to', n, 'are')
        counter = 0
        for num in range(0, n + 1):
            # prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    print(num, end=', ')
                    counter += 1
            else:
                return "Value is negative. Please provide positive number"
