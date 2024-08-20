class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark the numbers that appear by using the indices as a marker
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Collect all indices that are still positive (those numbers are missing)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
