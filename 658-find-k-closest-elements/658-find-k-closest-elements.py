class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr
        
        #run binary search to find the left index
        
        left = 0
        right = len(arr)-k
        
        while left < right:
            mid = (left + right) // 2
            
            #move the left pointer, distance is too big
            if x - arr[mid] > arr[mid + k] - x:
                left = mid +1
            else:
                right = mid
        
        return arr[left:left+k]