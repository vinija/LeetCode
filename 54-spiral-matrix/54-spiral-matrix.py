class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m , n = len(matrix), len(matrix[0])
        #refers to row as row can only move up or down
        topBound , bottomBound = 0, m-1
        #refers to cols as cols can only move right or left
        leftBound, rightBound = 0, n-1
        
        res = []
        size = m*n
        # we iterate until we have found the center
        #while leftBound <= rightBound and topBound <= bottomBound:       
        while len(res) < size:                    
            # runs through the first row straight through each col
            if topBound <= bottomBound:
                for col in range(leftBound, rightBound+1):
                    res.append(matrix[topBound][col])
                topBound += 1
            
            # next runs down the column
            if leftBound <= rightBound:
                for row in range(topBound, bottomBound+1):
                    res.append(matrix[row][rightBound])
                rightBound -= 1
            
            # goes right to left in col
            if topBound <= bottomBound:
                for col in range(rightBound, leftBound -1, -1):
                    res.append(matrix[bottomBound][col])
                bottomBound -= 1
            
            # goes up
            if leftBound <= rightBound:
                for row in range(bottomBound, topBound-1, -1):
                    res.append(matrix[row][leftBound])
                leftBound += 1
            
        return res  