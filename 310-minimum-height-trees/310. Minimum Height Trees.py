class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = [node for node in graph if len(graph[node]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves
