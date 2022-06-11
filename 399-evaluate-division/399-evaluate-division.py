class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        lenght = len(equations)
        for index in range(lenght):
            graph[equations[index][0]][equations[index][1]] = values[index]
            graph[equations[index][1]][equations[index][0]] = 1/values[index]
        
        def dfs(source, target, visited):
            if source not in graph or target not in graph: return -1
            
            if target in graph[source]:
                return graph[source][target]
            
            for index in graph[source]:
                if index not in visited:
                    visited.add(index)
                    temp = dfs(index,target, visited)
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[source][index]
            
            return -1
        
        output = []
        
        for p, q in queries:
            output.append(dfs(p,q, set()))
        
        return output
