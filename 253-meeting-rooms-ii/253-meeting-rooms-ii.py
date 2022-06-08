class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # One heap solution (equivalent to sorting), time complexity O(nlogn), space complexity O(n)
        heap = []
        for interval in intervals:
            heappush(heap, (interval[0], 1))
            heappush(heap, (interval[1], -1))
        meetings = 0
        num_rooms = 0
        while heap:
            meetings += heap[0][1]
            num_rooms = max(num_rooms, meetings)
            heappop(heap)
        return num_rooms