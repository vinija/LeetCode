class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and s[left].isalpha() == False:
                left += 1
            while left < right and s[right].isalpha() == False:
                right -= 1
            ans[left], ans[right] = ans[right], ans[left]         
            left += 1
            right -= 1
        return ''.join(ans)