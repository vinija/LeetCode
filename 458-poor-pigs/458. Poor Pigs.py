from math import log, ceil, isclose

class Solution:
    def poorPigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
        # Calculate the number of tests possible
        tests = minutes_to_test // minutes_to_die
        
        # Calculate the number of pigs required using logarithms
        pigs = log(buckets) / log(tests + 1)
        
        # Return the smallest integer greater than or equal to pigs
        return round(pigs) if isclose(pigs, round(pigs)) else ceil(pigs)
