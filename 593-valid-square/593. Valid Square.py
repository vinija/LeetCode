class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        # Store all six distances between the four points
        distances = [
            dist(p1, p2), dist(p1, p3), dist(p1, p4),
            dist(p2, p3), dist(p2, p4), dist(p3, p4)
        ]
        
        # Sort the distances
        distances.sort()
        
        # Check the first four distances (sides of the square) are equal and non-zero
        # and check the last two distances (diagonals) are equal
        return 0 < distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]
