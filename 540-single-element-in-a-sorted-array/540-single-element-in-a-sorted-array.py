class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        output = freq.most_common()[-1]
        return output[0]