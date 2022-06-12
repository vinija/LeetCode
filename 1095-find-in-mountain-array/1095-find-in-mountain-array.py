# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        peak = self.getPeak(arr)
        first = self.binary_search(arr, 0, peak-1, target)
        if first != -1: return first
        second = self.binary_search_rev(arr, peak, arr.length() - 1, target)
        return second
        
    def getPeak(self, arr):
        start, end = 0, arr.length() - 1
        while start < end:
            mid = (start + end) // 2
            if mid != 0:
                if arr.get(mid) > arr.get(mid - 1): start = mid + 1
                else: end = mid - 1
            else:
                if arr.get(mid) < arr.get(mid + 1): start = mid + 1
                else: end = mid - 1
        return end
        
    def binary_search(self, arr, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            val = arr.get(mid)
            if val == target: return mid
            elif val > target: end = mid - 1
            else: start = mid + 1
        return -1
    
    def binary_search_rev(self, arr, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            val = arr.get(mid)
            if val == target: return mid
            elif val > target: start = mid + 1
            else: end = mid - 1
        return -1