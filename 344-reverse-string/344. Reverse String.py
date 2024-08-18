class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        sLen = len(s) - 1
        t = [None] * len(s)

        for i in range(len(s)):
            t[sLen] = s[i]
            sLen -=1


        for i in range(len(s)):
            s[i] = t[i]
        