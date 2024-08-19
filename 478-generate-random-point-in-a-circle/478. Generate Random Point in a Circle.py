import random
import math
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        # Initialize the circle's properties
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Generate a random radius within the circle
        r = math.sqrt(random.random()) * self.radius
        
        # Generate a random angle between 0 and 2π
        theta = random.uniform(0, 2 * math.pi)
        
        # Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
