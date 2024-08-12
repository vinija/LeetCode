import heapq

class MedianFinder:

    def __init__(self):
        # max heap to store smaller half of data
        self.lower_half = []

        #min heap to store the larger half of the data
        self.upper_half = []
        

    def addNum(self, num: int) -> None:
        # Python is a min heap by default thus negative
        heapq.heappush(self.lower_half, -num)

        #Condition: The largest element in lower half is <= smallest element in upper half
        if self.lower_half and self.upper_half and (-self.lower_half[0] > self.upper_half[0]):
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        
        #Balance the size of the two heaps
        if len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
        
        elif len(self.upper_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))
        

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return -self.lower_half[0]
        else:
            return (-self.lower_half[0] + self.upper_half[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()