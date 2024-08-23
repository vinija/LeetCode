class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        #handle edge cases where k is even or divisible by 5
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 1 % k #init the remainder
        lenght = 1 #init with smallest length
        seen_remainders = set() # track remainder

        while remainder != 0:
            if remainder in seen_remainders:
                return -1 # cycle detected, no valid n
            
            seen_remainders.add(remainder)
            remainder = (remainder * 10 + 1) % k
            lenght += 1
        return lenght