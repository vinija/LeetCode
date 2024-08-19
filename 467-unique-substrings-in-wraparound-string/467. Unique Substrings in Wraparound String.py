class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:

        max_len_end_with = {ch: 0 for ch in 'abcdefghijklmnopqrstuvwxyz'}

        max_len_current = 0

        for i in range(len(s)):

            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and s[i] == 'a')):
                max_len_current += 1
            else:
                max_len_current = 1
        
            max_len_end_with[s[i]] = max(max_len_end_with[s[i]], max_len_current)
    
        return sum(max_len_end_with.values())
        