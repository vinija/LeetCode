class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Start by sorting the inputs
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Consider the edges first
        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            # horizontalCuts[i] - horizontalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible height
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])
        
        # Consider the edges first
        max_width = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            # verticalCuts[i] - verticalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible width
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])
        
        # Python doesn't need to worry about overflow - don't forget the modulo though!
        return (max_height * max_width) % (10**9 + 7)