from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    	return list(Counter(t) - Counter(s))[0]