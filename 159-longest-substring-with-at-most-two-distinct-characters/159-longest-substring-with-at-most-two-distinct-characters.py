class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        seen = Counter()
        maxCount = 0
        
        for end, char in enumerate(s):
            seen[char] +=1
            while len(seen)>2:
                leftChar = s[start]
                seen[leftChar] -=1
                
                if seen[leftChar] == 0:
                    del seen[leftChar]
                
                start +=1
            
            maxCount = max(maxCount, end - start +1)
        
        return maxCount

    
