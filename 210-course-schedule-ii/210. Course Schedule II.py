from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == numCourses:
            return order
        else:
            return []
        
        