class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:
        #check overlap w/ existing bookings

        for s, e in self.bookings:
            if max(s, start) < min(e, end):
                return False
        
        self.bookings.append((start,end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)