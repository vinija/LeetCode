class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n #initialize the array result with 1's

        #Calculate left product and store in result
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        #Calculate right product and store in result
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result



        return result
        