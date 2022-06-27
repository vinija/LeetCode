class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        num = float('-inf')
        for n in nums[::-1]:
            
            while stack and stack[-1] < n:
                num = stack.pop()
            if n < num:
                return True
            stack.append(n)
        return False