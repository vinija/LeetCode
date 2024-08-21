class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        start, end = len(nums), 0

        #compare each element in original array with sorted array
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        
        return end - start + 1 if end - start >= 0 else 0