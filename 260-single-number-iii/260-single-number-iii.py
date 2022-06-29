class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n= 2
        output = counter.most_common()[:-n-1:-1]
        ret = []
        for item, freq in output:
            ret.append(item)
        
        return ret
        