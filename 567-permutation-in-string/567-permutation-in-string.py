class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_c = Counter(s1)
        
        for i in range(len(s2)-window+1):
            s2_c = Counter(s2[i:i+window])
            if s2_c == s1_c:
                return True
            
        return False