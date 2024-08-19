from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        
        if originalColor == newColor:
            return image
        
        # Queue for BFS
        queue = deque([(sr, sc)])
        
        while queue:
            r, c = queue.popleft()
            
            # Fill the current pixel with the new color
            image[r][c] = newColor
            
            # Iterate over the four directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                # If the neighboring pixel is within bounds and matches the original color
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == originalColor:
                    queue.append((nr, nc))
        
        return image
