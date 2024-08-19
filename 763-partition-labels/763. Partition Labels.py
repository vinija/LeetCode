from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_occurence = {char: i for i, char in enumerate(s)}

        partitions = []
        start = end = 0

        for i, char in enumerate(s):
            end = max(end, last_occurence[char])
            if i == end:
                partitions.append(end - start +1)
                start = i + 1
        
        return partitions
        