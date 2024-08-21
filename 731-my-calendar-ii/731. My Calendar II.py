from typing import List

class MyCalendarTwo:

    def __init__(self):
        self.calendar = [] #single booking
        self.overlaps = [] #double booking
        

    def book(self, start: int, end: int) -> bool:
        #check triple booking case first
        for os, oe in self.overlaps:
            if start < oe and end > os:
                return False
        
        for cs, ce in self.calendar:
            if start < ce and end > cs:
                self.overlaps.append((max(start,cs), min(end,ce)))
        self.calendar.append((start,end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)