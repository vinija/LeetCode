class MyCalendarTwo:

    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []
        

    def book(self, start: int, end: int) -> bool:

        for s, e in self.double_bookings:
            if start < e and end > s:
                return False
        
        for s, e in self.single_bookings:
            if start < e and end > s:
                self.double_bookings.append((max(start,s), min(end, e)))
        
        self.single_bookings.append((start,end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)