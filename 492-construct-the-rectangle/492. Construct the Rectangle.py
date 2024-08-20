from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start with the largest possible square root value for L
        W = int(math.sqrt(area))
        
        # Find the largest W such that area % W == 0 and L >= W
        while area % W != 0:
            W -= 1
        
        # L is determined by area / W
        L = area // W
        
        return [L, W]
