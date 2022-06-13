class Solution:
       def countPrimes(self, n: int) -> int:

        #Initial Edge Cases (0, 1 non-prime by definition)

        if n <= 2:
            return 0

        #population of list for classification of primes
        #all numbers initialized as prime, and then discounted via 'Sieve of Eratosthenes' algorithm
        #naturally, our list is of size(n)

        primes = [True] * n
        primes[0] = primes[1] = False 

        #for all elements in the range [2 , n)
        for number in range(2, n):

            #if it is a prime 
            if primes[number]:

                #starting from 2 * prime and ending at n - in increments of prime
                for multiple in range(2 * number, n, number):


                #change index accounting for prime validity to 'False' or every multiple of found prime.
                #we can correctly categorize a large number of composite numbers due to the fact that our first 
                #prime is undoubtly a factor of all larger multiples of the same number.

                    primes[multiple] = False


        #Sum of Total Booleans             
        return sum(primes)