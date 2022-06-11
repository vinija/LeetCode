class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
         if len(s) == len(goal) and goal in s+s:
                return True