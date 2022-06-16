class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # One heap solution (equivalent to sorting), time complexity O(nlogn), space complexity O(n)
        heap = []
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        for meeting in intervals:
            if not heap:
                heapq.heappush(heap, meeting[1])
            else:
                if meeting[0] >= heap[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, meeting[1])
        
        return len(heap)