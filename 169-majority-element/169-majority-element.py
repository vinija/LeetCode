class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        item = freq.most_common()
        
        return item[0][0]