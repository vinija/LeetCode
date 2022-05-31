class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for item,value in counter.items():
            if value ==1:
                return item
        
        return 0
        