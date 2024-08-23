from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #List to hold all pickup dropoff events
        events = []

        # Create events for all trips
        for num_passengers, start, end in trips:
            events.append((start, num_passengers)) #pickup event
            events.append((end, -num_passengers)) #drop off
        
        #if same location, sort by drop offs first
        events.sort()

        current_passengers = 0

        #process all the events
        for location, passenger_change in events:
            current_passengers += passenger_change
            #if at any point the capacity is exceeded, return False
            if current_passengers > capacity:
                return False
        
        return True