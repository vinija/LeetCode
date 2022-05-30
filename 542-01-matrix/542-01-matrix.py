class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		Row, Col = len(mat), len(mat[0])
		queue = []
		directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

		for i in range(Row):
			for j in range(Col):
				if mat[i][j] == 0:
					queue.append((i, j)) 
				else:
					mat[i][j] = "*"

		for r, c in queue:
			for dr, dc in directions:
				row = r + dr
				col = c + dc
				if 0 <= row < Row and 0 <= col < Col and mat[row][col] == "*":
					mat[row][col] = mat[r][c] + 1
					queue.append((row, col))
		return mat