class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     x = x * -1
        
        stringX = str(x)
        return stringX == stringX[::-1]
        
        
        