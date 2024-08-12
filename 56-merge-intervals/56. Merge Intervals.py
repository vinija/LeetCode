from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])

        #initialize the results list
        merged = []

        for interval in intervals:
            #append if merged list is empty or no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                #overlap exists, merge
                merged[-1][1] = max(merged[-1][1], interval[1])
            

        return merged
        