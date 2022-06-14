class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n 
        sorted_nums = sorted(nums)
        
        for i in range(n):
            #binary search, locate the insertion point of x in nums
            index = bisect.bisect_left(sorted_nums, nums[i])
            print(index)
            counts[i] = index
            del sorted_nums[index]
        return counts
