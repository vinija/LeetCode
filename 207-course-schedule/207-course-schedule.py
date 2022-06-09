from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree_list = defaultdict(int)

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        for prerequisite in prerequisites:
            take_course = prerequisite[0]
            dependent_course = prerequisite[1]
            self.graph[dependent_course].append(take_course)
            if dependent_course not in self.in_degree_list:
                self.in_degree_list[dependent_course] = 0
            self.in_degree_list[take_course] += 1

        in_degree_zero_found = True
        while len(self.in_degree_list) > 0:
            in_degree_zero_found = False
            for in_degree_node in self.in_degree_list:
                in_degree = self.in_degree_list[in_degree_node]
                if in_degree == 0:
                    in_degree_zero_found = True
                    # Remove this in_degree_node and and decrement all the adjacency's of in_degree_node by 1
                    del self.in_degree_list[in_degree_node]
                    adj_list = self.graph[in_degree_node]
                    for adj_node in adj_list:
                        if adj_node in self.in_degree_list:
                            self.in_degree_list[adj_node] -= 1
                    break
            if not in_degree_zero_found:
                return False
        if len(self.in_degree_list) == 0:
            return True
        return False

numCourses = 4
prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]
prerequisites = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
sol = Solution()
print(sol.canFinish(numCourses, prerequisites))