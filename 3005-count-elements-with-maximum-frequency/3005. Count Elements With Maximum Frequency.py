from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        highestFreq = 0

        counts = Counter(nums)

        for index, value in enumerate(counts):
            if(counts.get(value) > highestFreq):
                highestFreq = counts.get(value)
                ans = highestFreq
            elif counts.get(value) == highestFreq:
                ans += counts.get(value)

        return ans
        