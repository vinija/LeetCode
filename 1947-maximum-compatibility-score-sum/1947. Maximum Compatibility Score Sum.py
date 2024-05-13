from typing import List

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        
        # Calculate compatibility score for each student-mentor pair
        compatibility = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                compatibility[i][j] = sum(students[i][k] == mentors[j][k] for k in range(n))
        
        # Memoization dictionary
        memo = {}
        
        # DFS function to try every assignment using bitmasking
        def dfs(mask):
            if mask == (1 << m) - 1:  # All students are assigned
                return 0
            if mask in memo:
                return memo[mask]
            
            # Determine the next student index to assign
            student_index = bin(mask).count('1')
            max_score = 0
            
            # Try assigning current student to any unassigned mentor
            for mentor_index in range(m):
                if not (mask & (1 << mentor_index)):  # Check if this mentor is unassigned
                    # Assign and calculate score recursively
                    new_score = compatibility[student_index][mentor_index] + dfs(mask | (1 << mentor_index))
                    max_score = max(max_score, new_score)
            
            memo[mask] = max_score
            return max_score
        
        # Start DFS with no students assigned
        return dfs(0)

# Example usage
sol = Solution()
students = [[1,1,0],[1,0,1],[0,0,1]]
mentors = [[1,0,0],[0,0,1],[1,1,0]]
print(sol.maxCompatibilitySum(students, mentors))  # Output: 8
