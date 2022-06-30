class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
        return seen.pop()