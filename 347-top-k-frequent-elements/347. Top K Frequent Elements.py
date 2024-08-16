from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key = count.get)