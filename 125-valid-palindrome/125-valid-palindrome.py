class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = s.replace(" ", "")
        s = s.lower()
        r = ""
        for x in s:
            if x.isalnum():
                r += x
        return r == r[::-1]