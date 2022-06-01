class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1 # starting from 1 digit
        while n > 9*base*digit: # upper limit of d digits 
            n -= 9*base*digit
            digit += 1
            base *= 10 
        q, r = divmod(n-1, digit)
        return int(str(base + q)[r])