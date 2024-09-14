from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        p_count = Counter(p)
        s_count = Counter()
        p_length = len(p)

        for i in range(len(s)):
            #Add character to current sliding window
            s_count[s[i]] += 1

            #remove character that is left out of the sliding window
            if i >= p_length:
                if s_count[s[i - p_length]] == 1:
                    del s_count[s[i - p_length]] #Remove character completely if count is zero
                else:
                    s_count[s[i - p_length]] -= 1
            
            #compare counters to check for anagram
            if s_count == p_count:
                result.append(i - p_length + 1)
        



        return result