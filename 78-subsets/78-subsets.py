class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rSet = []
        if len(nums) == 0:
            return [[]]
        x = nums[0]
        y = self.subsets(nums[1:])
        # rSet = y
        for i in y:
            rSet.append(i)
            rSet.append([x]+ i)
        return rSet


