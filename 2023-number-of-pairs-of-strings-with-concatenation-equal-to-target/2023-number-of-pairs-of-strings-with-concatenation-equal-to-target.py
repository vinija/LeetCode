
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        freq = collections.Counter(nums)
        # print(freq)

        for e in freq:
            # print(target[:len(e)], target[len(e):] )
            if target[:len(e)] == e:
                suffix = target[len(e):]
                ans += freq[e] * freq[suffix]
                if e == suffix:
                    ans -= freq[suffix]

        return ans