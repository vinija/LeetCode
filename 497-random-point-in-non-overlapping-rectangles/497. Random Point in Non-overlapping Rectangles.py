import random
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        self.total_area = 0

        # Calculate cumulative areas
        for rect in rects:
            x1, y1, x2, y2 = rect
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.total_area += area
            self.areas.append(self.total_area)

    def pick(self) -> List[int]:
        # Pick a random point by first selecting a rectangle
        rand_area = random.randint(1, self.total_area)

        # Binary search to find the rectangle corresponding to rand_area
        low, high = 0, len(self.areas) - 1
        while low < high:
            mid = (low + high) // 2
            if self.areas[mid] < rand_area:
                low = mid + 1
            else:
                high = mid

        # We have identified the rectangle in which to pick a point
        rect = self.rects[low]
        x1, y1, x2, y2 = rect

        # Randomly pick a point within the chosen rectangle
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]
