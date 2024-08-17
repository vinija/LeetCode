class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Divide n by 2, 3, and 5 as long as it's divisible by them
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        
        # If n becomes 1, it's an ugly number
        return n == 1
