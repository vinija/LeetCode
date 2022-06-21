class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        seen = 0
        for c in t:
            if s[seen] == c:
                seen += 1
            if seen == len(s):
                return True
        return False