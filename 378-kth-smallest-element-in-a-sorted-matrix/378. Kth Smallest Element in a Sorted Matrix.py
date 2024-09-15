class Solution(object):
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def count_less_equal(matrix, smaller, mid, larger):
            count, n = 0, len(matrix)
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                  # as matrix[row][col] is bigger than the mid, let's keep track of the
                  # smallest number greater than the mid
                  larger = min(larger, matrix[row][col])
                  row -= 1
                else:
                  # as matrix[row][col] is less than or equal to the mid, let's keep track of the
                  # biggest number less than or equal to the mid
                  smaller = max(smaller, matrix[row][col])
                  count += row + 1
                  col += 1

            return count, smaller, larger
            
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2 # or l + (r - l) // 2
            
            # calculate how many numbers are on the left of middle number
            count, smaller, larger = count_less_equal(matrix, l, mid, r)
            # or order = sum(bisect.bisect(row, m) for row in matrix) < k:  
            
            if count >= k:
                r = smaller # search lower
            else:
                l = larger # search higher
                
        return l