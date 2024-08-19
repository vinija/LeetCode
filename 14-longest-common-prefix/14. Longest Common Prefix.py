class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        strs.sort()

        #compare first and last string
        first = strs[0]
        last = strs[-1]
        i = 0

        #compare chars
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]
        