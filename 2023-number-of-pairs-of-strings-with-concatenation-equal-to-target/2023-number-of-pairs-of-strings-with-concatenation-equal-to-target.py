class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ctr = Counter(nums)
        return sum(ctr[prefix] * (ctr[suffix] - (prefix == suffix))
                   for prefix in accumulate(target)
                   for suffix in [target.removeprefix(prefix)])