class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # Process current asteroid
            while stack and asteroid < 0 < stack[-1]:
                # Compare the last asteroid in the stack with the current one
                if stack[-1] < -asteroid:
                    stack.pop()  # Right-moving asteroid in stack is smaller and gets destroyed
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both asteroids destroy each other
                break
            else:
                stack.append(asteroid)  # If no collision, or current asteroid survives, add to stack
        
        return stack
