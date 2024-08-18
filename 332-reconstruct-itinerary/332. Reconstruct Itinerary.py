from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Step 1 build the graph
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)


        #Step 2 list to store itinerary, will be returned
        itinerary = []

        #Step 3 Define DFS function
        def dfs(airport):
            #visit all the destination from current airport in lexical order
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                dfs(next_dest)
            
            itinerary.append(airport)

        #Step 4 Start DFS from JFK
        dfs("JFK")

        #Step 5 Reverse itinerary since DFS will return reverse order and return
        return itinerary[::-1]
        