class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        answer = matrix.copy()
        for i in range(n):
            maxi=0
            for j in range(m):
                maxi=max(maxi, answer[j][i])
            for j in range(m):
                if answer[j][i] == -1:
                    answer[j][i] = maxi
        return answer