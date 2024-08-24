class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1, min2 = inf, inf
        for n in islice(nums, 1, None):
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        return nums[0] + min1 + min2       