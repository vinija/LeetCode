from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Initialize graph and in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        # Step 2: Build the graph and fill the in-degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Step 3: Initialize the queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Step 4: Process the courses
        taken_courses = 0
        while queue:
            current = queue.popleft()
            taken_courses += 1
            
            # Decrease the in-degree of dependent courses
            for next_course in graph[current]:
                in_degree[next_course] -= 1
                # If in-degree becomes zero, add it to the queue
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # Step 5: Check if all courses have been taken
        return taken_courses == numCourses
