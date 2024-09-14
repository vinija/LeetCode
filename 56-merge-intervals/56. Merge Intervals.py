from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals or len(intervals) == 1:
            return intervals
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        merged = []

        for index, current in enumerate(sorted_intervals):
            current_start, current_end = current

            if not merged:
                merged.append([current_start, current_end])
                continue
            
            last_merged_start, last_merged_end = merged[-1]

            if current_start <= last_merged_end:
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                merged.append([current_start, current_end])
        return merged
        
        