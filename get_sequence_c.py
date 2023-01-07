import time
import unittest

# start_time = time.perf_counter()
def get_sequence_c(a: list, b: list) -> list:
    """
        Function get_sequence_c returns sequence c, that contain all 
        elements from sequence A (maintaining the order) except those, 
        that are present in sequence B p times, where p is a prime number. 

        Args:
        a: list of integers
        b: list of integers

        Returns:
        c: list of integers
    """
    def is_prime(n: int) -> bool:
        """
            Function is_prime, checks if given number is prime or not by using Sieve of Eratosthenes.

            Args: 
            n: integer

            Returns:
            primes[n]: bool
        """        
        if n < 2:
            return False
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i ** 2, n + 1, i):
                    primes[j] = False
        return primes[n]

    c = []
    for x in a:
        if x not in b or not is_prime(b.count(x)):
            c.append(x)
    return c
# end_time = time.perf_counter()

# elapsed_time = end_time - start_time
"""
    Unittests to check that get_sequence_c works appropriate :)
"""
class Test_get_sequence_c(unittest.TestCase):

    def test_get_sequence_c(self):
        self.assertEqual(get_sequence_c([2,3,9,2,5,1,3,7,10], [2,1,3,4,3,10,6,6,1,7,10,10,10]), [2,9,2,5,7,10])
        self.assertEqual(get_sequence_c([1,1,1,1], [1,1,1,1,1,1,1,1]), [1,1,1,1])
        self.assertEqual(get_sequence_c([1,2,3,4,5], [1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(get_sequence_c([1,2,3,4,5], [6,7,8,9,10]), [1,2,3,4,5])
    
    def test_get_sequence_c_empty_list(self):
        self.assertEqual(get_sequence_c([], [1,2,3,4,5]),[])
        self.assertEqual(get_sequence_c([1,2,3,4,5], []),[1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()