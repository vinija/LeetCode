class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i%n]:
                index = stack.pop()
                res[index] = nums[i % n]
            
            if i < n:
                stack.append(i)
        
        return res