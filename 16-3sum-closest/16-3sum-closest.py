class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = math.inf
        r = None 
        nums.sort()
        n = len(nums)
        print(nums)
        
        for i in range(n):
            lo = i + 1
            hi = n - 1
            while lo < hi:
                csum = nums[i] + nums[lo] + nums[hi]
                diff = abs(csum - target)
                if diff < min_diff:
                    min_diff = diff
                    r = csum
                if csum < target:
                    lo += 1
                elif csum > target:
                    hi -= 1
                else:
                    return r
        return r 