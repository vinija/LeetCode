# time: O(n^2)
# space: O(n) to store visit list

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
       
        if not M:
            return 0
        
        n = len(M)
        visit = [False]*n
        
        def dfs(u):
            for v in range(n):
                if M[u][v] ==1 and visit[v] == False:
                    visit[v] = True
                    dfs(v)
        
        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                dfs(i)
        
        return count