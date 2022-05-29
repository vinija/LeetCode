class Solution:
    
    def twoSum(self, nums, target):
        
        nums_hash = {}
        for i, num in enumerate(nums):
            potentialMatch = target - num
            if potentialMatch in nums_hash:
                return [nums_hash[potentialMatch], i]
            nums_hash[num] = i
      