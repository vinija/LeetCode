class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Adjust the hour to be within 12-hour format (since 12 should be treated as 0)
        if hour == 12:
            hour = 0
        
        # Calculate the angle for the minute hand (6 degrees per minute)
        minute_angle = minutes * 6
        
        # Calculate the angle for the hour hand (30 degrees per hour + 0.5 degrees per minute)
        hour_angle = hour * 30 + minutes * 0.5
        
        # Find the difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # The smaller angle between the two hands is either the calculated angle or 360 - angle
        return min(angle, 360 - angle)

