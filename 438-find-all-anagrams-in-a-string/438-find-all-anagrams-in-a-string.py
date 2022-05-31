class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        windowStart = 0
        matched = 0
        charFrequency = {}
        
        for char in p:
            if char not in charFrequency:
                charFrequency[char] = 0
            charFrequency[char] += 1
        
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar in charFrequency:
                charFrequency[rightChar] -= 1
                if charFrequency[rightChar] == 0:
                    matched += 1
                    
            if matched == len(charFrequency):
                indices.append(windowStart)
                
            if windowEnd >= len(p) - 1:
                leftChar = s[windowStart]
                windowStart += 1
                if leftChar in charFrequency:
                    if charFrequency[leftChar] == 0:
                        matched -= 1
                    charFrequency[leftChar] += 1
                    
        return indices