class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for index, value in enumerate(nums):
            if (length <= 1) or (nums[length-2] != value):
                nums[length] = value
                length +=1
        
        return length