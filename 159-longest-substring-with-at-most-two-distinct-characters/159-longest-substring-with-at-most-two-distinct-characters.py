class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = Counter()
        start = 0
        maxCount = 0
        
        # sliding window from start to end
        for end, char in enumerate(s):
            # saw a char? add it to our hashmap
            seen[char] += 1
            
            # do you have more chars than what we need?
            while len(seen) > 2:
                # start removing character from left
                leftChar = s[start]
                seen[leftChar] -= 1
                
                # if count for a char is 0, delete it from our hashmap
                if seen[leftChar] == 0:
                    del seen[leftChar]
                    
                # move the left pointer ahead
                start += 1
                
            # current window
            count = end - start + 1
            maxCount = max(count, maxCount)
        
        return maxCount