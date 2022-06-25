class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        
        ######## O(n^3) solution ########
        # return sum(
        #     max( nums[i:j+1] ) - min( nums[i:j+1] )
        #         for i in range(n)
        #             for j in range(i,n)
        # )
        
        ######## O(n^2) solution ########
        # res = 0
        # for i in range(n):
        #     currMax = currMin = nums[i]
        #     for j in range(i+1,n): 
        #         currMax, currMin = max(currMax, nums[j]), min(currMin, nums[j])
        #         res += (currMax - currMin)
        # return res
    
        ######## O(n) solution ########
        # tie-breaking by taking the left-most index...
        # for each i = 1, ..., n-2, find left and right
        res = 0
        for i in range(n):
            for left in range(i, -1, -1):
                if left == 0 or nums[left-1] >= nums[i]:
                    break
            for right in range(i, n):
                if right == n-1 or nums[right+1] > nums[i]: 
                    break
            res += nums[i] * (i - left + 1) * (right - i + 1)
        
        for i in range(n):
            for left in range(i, -1, -1):
                if left == 0 or nums[left-1] <= nums[i]:
                    break
            for right in range(i, n):
                if right == n-1 or nums[right+1] < nums[i]:
                    break
            res -= nums[i] * (i - left + 1) * (right - i + 1)
        
        return res
            