class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 4 == 0:
            n //= 4
        
        return n == 1
        