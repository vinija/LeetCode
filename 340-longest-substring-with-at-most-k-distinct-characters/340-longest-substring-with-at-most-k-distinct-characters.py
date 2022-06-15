class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        start = 0
        maxCount = 0
        
        for end,char in enumerate(s):
            
            seen[char] +=1
            
            
            while len(seen) > k:
                #start removing character from left
                leftChar = s[start]
                seen[leftChar]-=1
                
                if seen[leftChar]== 0:
                    del seen[leftChar]
                start +=1
            count = end - start+1
            maxCount = max(count,maxCount)
        
        return maxCount