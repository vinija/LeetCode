class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        #Calculate the min number of repeats
        min_repeats = (len(b) + len(a) - 1) // len(a)

        # Check if b is a substring of the repeated string
        if b in a * min_repeats:
            return min_repeats
        
        if b in a * (min_repeats + 1):
            return min_repeats + 1
        
        return -1
        