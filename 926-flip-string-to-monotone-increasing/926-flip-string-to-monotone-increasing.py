# Keep track of zero and one. Since this is an increasing, the left side would likely be 'zero', hence while iterating through the string, all the leading zero(s) will be ignored (set count_zero to count_one, which is zero because we have not hit any 'one' yet). Once we starts hitting 'one', then the logic will compute which one has the majority of the population. The minority should be flipped accordingly.

class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:
        
        count_one = 0
        count_zero = 0

        for i in range(len(s)):
            if s[i] == '0':
                count_zero += 1
            else:
                count_one += 1
            # ignore leading 'zero' while counting.  Once hits 'one', count population and return the minority to get the minimum flipping needed. 
            if count_zero > count_one:
                count_zero = count_one
        
        return count_zero