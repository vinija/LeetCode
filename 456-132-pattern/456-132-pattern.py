class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        
        second_num = -math.inf
        stck = []
        # Try to find nums[i] < second_num < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_num:
                return True
            # always ensure stack can be popped in increasing order
            while stck and stck[-1] < nums[i]:
                second_num = stck.pop()  # this will ensure  second_num < stck[-1] for next iteration

            stck.append(nums[i])
        return False