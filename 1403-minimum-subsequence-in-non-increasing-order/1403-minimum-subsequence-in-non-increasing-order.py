class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        while sum(res) <= sum(nums):
            res.append(nums.pop())
        return res   