from collections import defaultdict

class MyCalendarThree:

    def __init__(self):
        self.delta = defaultdict(int)
        

    def book(self, startTime: int, endTime: int) -> int:

        self.delta[startTime] += 1
        self.delta[endTime] -= 1

        ongoing_events = 0
        max_overlap = 0

        for time in sorted(self.delta):
            ongoing_events += self.delta[time]
            max_overlap = max(max_overlap, ongoing_events)
        
        return max_overlap
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)