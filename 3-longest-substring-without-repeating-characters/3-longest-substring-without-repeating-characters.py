class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        counter = Counter()
        longLen = 0
        
        for right,value in enumerate(s):
            counter[value] +=1
            while counter[value] > 1:
                counter[s[left]] -=1
                left +=1
            longLen = max(longLen, right-left+1)
        
        return longLen
