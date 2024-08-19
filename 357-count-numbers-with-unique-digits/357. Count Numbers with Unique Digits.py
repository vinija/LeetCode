class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        # Start with 10 for n = 1 (0 through 9)
        count = 10
        
        # Initial product of choices for n = 2
        product = 9
        
        # For calculating unique digits for 2, 3, ... n
        for i in range(1, n):
            product *= (10 - i)
            count += product
        
        return count
