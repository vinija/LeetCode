class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = min(strs, key = len)
        
        for s in strs:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
        
        return prefix