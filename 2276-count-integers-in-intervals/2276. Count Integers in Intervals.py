from sortedcontainers import SortedDict

class CountIntervals:

    def __init__(self):
        self.intervals = SortedDict()
        self.total_count = 0

    def add(self, left: int, right: int) -> None:
        intervals = self.intervals
        
        # Find the position of the new interval
        start = intervals.bisect_left(left)
        end = intervals.bisect_right(right)
        
        # Adjust the boundaries of the new interval
        new_left = left
        new_right = right
        
        if start > 0 and intervals.peekitem(start-1)[1] >= left - 1:
            start -= 1
            new_left = intervals.peekitem(start)[0]
        
        if end > 0 and intervals.peekitem(end-1)[1] >= right - 1:
            new_right = max(right, intervals.peekitem(end-1)[1])
        
        # Remove all intervals that are merged into the new one
        for i in range(start, end):
            l, r = intervals.popitem(start)
            self.total_count -= r - l + 1
        
        # Add the new merged interval
        intervals[new_left] = new_right
        self.total_count += new_right - new_left + 1

    def count(self) -> int:
        return self.total_count
