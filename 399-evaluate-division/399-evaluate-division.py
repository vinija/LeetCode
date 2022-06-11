class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #directed graph
        graph = defaultdict(dict)
        lenght = len(equations)
        for index in range(lenght):
            #we're building out our graph with all the connections, a->b b->a,-> c
            #from our target, if target *2 = value
            graph[equations[index][0]][equations[index][1]] = values[index]
            #we need inverse relationship as well, which is 1/value
            graph[equations[index][1]][equations[index][0]] = 1/values[index]
        
        def dfs(source, target, visited):
            #these values dont even exist in our graph
            if source not in graph or target not in graph: return -1
            
            #we found it already
            if target in graph[source]:
                return graph[source][target]
            
            
            for index in graph[source]:
                if index not in visited:
                    visited.add(index)
                    #start the search with index as the source
                    temp = dfs(index,target, visited)
                    #we didn't find anything
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[source][index]
            
            return -1
        
        output = []
        
        for p, q in queries:
            output.append(dfs(p,q, set()))
        
        return output
