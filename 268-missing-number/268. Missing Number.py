class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the expected sum of the first n natural numbers (0 to n)
        expected_sum = n * (n + 1) / 2
        # Calculate the actual sum of numbers in the array
        actual_sum = sum(nums)
        # The difference between the expected sum and the actual sum is the missing number
        return int(expected_sum - actual_sum)
