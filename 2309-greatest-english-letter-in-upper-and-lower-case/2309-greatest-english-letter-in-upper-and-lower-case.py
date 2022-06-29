class Solution:
    def greatestLetter(self, s: str) -> str:
            c="abcdefghijklmnopqrstuvwxyz"
            l=[""]
            for lowercase in c:
                if lowercase in s and lowercase.upper() in s:
                    l.append(lowercase.upper())
            l.sort()
            return l[-1]
