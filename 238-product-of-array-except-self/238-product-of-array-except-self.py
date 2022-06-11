class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        
        for index in range(len(nums)):
            output[index] *= prefix
            prefix *= nums[index]
        
        suffix = 1
        
        for sufIndex in range(len(nums)-1,-1,-1):
            output[sufIndex] *= suffix
            suffix *= nums[sufIndex]
        
        return output