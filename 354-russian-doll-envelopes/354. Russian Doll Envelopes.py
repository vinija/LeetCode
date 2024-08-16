from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #sort envelopes by width in asceding, if same width, sort height by descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        #extract heights 
        heights = [envelope[1] for envelope in envelopes]

        #find longest increasing subsequence for heights
        result = []

        for height in heights:

            index = bisect.bisect_left(result, height)
            if index == len(result):
                result.append(height)
            else:
                result[index] = height



        return len(result)
        