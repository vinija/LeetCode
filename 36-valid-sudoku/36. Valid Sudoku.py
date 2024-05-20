class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to keep track of seen numbers in rows, columns, and 3x3 sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    # Calculate box index
                    box_index = (i // 3) * 3 + (j // 3)
                    
                    # Check if the number is already seen in the current row, column, or box
                    if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                        return False
                    
                    # Add the number to the corresponding row, column, and box sets
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)

        return True

        