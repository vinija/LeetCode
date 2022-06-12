from queue import PriorityQueue 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        for num in nums:
            pq.put(num)
            
        numNeed = len(nums) - k
        
        while pq and numNeed > 0:
            print(pq.get())
            numNeed-=1
            print(k)
            
        
        return pq.get()
        
        
        