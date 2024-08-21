class MyCalendarThree:

    def __init__(self):
        # Initialize a dictionary to keep track of all events
        # The key is the time (start or end), and the value is the number of events starting or ending at that time
        self.events = {}

    def book(self, startTime: int, endTime: int) -> int:
        # Increase the count of events starting at `startTime`
        if startTime in self.events:
            self.events[startTime] += 1
        else:
            self.events[startTime] = 1
        
        # Decrease the count of events ending at `endTime`
        if endTime in self.events:
            self.events[endTime] -= 1
        else:
            self.events[endTime] = -1
        
        # Traverse through the events to find the maximum number of overlapping events
        ongoing = 0
        max_overlap = 0
        for time in sorted(self.events):
            ongoing += self.events[time]
            max_overlap = max(max_overlap, ongoing)
        
        return max_overlap
