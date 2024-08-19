class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Step 1: Double the string and remove the first and last character
        doubled_s = (s + s)[1:-1]
        
        # Step 2: Check if the original string is a substring of the modified doubled string
        return s in doubled_s
