class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o = 0
        c = 0

        for char in s:
            if char == "(":
                o += 1
            elif char == ')':
                if o > 0:
                    o -= 1
                else:
                    c += 1
        return o + c
        