from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        #check if points is empty
        if not points:
            return 0
        
        #step 2: sort the points based on end position of each interval
        points.sort(key=lambda x: x[1])

        #step 3: initialize the number of arrows needed
        arrows = 1

        current_end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > current_end:
                arrows +=1
                current_end = points[i][1]
        
        return arrows
        