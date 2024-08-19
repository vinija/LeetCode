from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        sum12 = Counter()

        for a in nums1:
            for b in nums2:
                sum12[a+b] += 1
        
        count = 0

        for c in nums3:
            for d in nums4:
                count += sum12.get(-(c + d), 0)
        
        return count
        