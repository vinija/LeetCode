# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        # Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = 0, 0
        dir_idx = 0

        current = head

        while current:
            matrix[r][c] = current.val
            current = current.next

            next_r = r + directions[dir_idx][0]
            next_c = c + directions[dir_idx][1]

            # Check if the next position is within bounds and the cell is not filled yet
            if 0 <= next_r < m and 0 <= next_c < n and matrix[next_r][next_c] == -1:
                r, c = next_r, next_c
            else:
                # Change direction
                dir_idx = (dir_idx + 1) % 4
                r += directions[dir_idx][0]
                c += directions[dir_idx][1]
        
        return matrix

