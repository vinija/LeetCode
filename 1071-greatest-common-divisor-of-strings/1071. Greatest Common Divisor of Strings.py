class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #check if str1 + str2 == str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]