class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        twoIndex = 0
        for index in range(m, len(nums1)):
            nums1[index] = nums2[twoIndex]
            twoIndex+=1
        
        nums1[:] = sorted(nums1)