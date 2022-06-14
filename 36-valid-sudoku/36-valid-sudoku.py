class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        setRow = set()
        
        #each row
        for row in range(rows):
            setRow = set()
            for col in range(cols):
                if board[row][col] in setRow and board[row][col] not in ".," :
                    return False
                else:
                    setRow.add(board[row][col])
        
        #each col
        for col in range(cols):
            setCol = set()
            for row in range(rows):
                if board[row][col] in setCol and board[row][col] not in ".," :
                    return False
                else:
                    setCol.add(board[row][col])
                    
        boxes = [set() for _ in range(rows)]
        #each box [0-2, 3-5,6-8] 
        for row in range(rows):
            for col in range(cols):
                idx = (row // 3) * 3 + col // 3
                if board[row][col] in boxes[idx] and board[row][col] not in ".," :
                    return False
                else:
                    boxes[idx].add(board[row][col])
                
        
        return True
                
                