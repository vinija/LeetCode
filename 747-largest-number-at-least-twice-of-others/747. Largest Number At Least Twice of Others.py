class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        maxIndex = nums.index(maxNum)

        for i, num in enumerate(nums):
            if i != maxIndex and maxNum < 2 * num:
                return -1
        return maxIndex
        