class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        
        for key,value in freq.items():
            if value == 1:
                return s.index(key)
        
        return -1
        