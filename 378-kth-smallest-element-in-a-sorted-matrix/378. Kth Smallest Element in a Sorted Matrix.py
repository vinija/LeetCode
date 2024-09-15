class Solution(object):
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def findCount(matrix, val):
            count = 0
            for row in matrix:
                for col in row:
                    if col <= val: count += 1
            return count
            
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2 # or l + (r - l) // 2
            
            # calculate how many numbers are on the left of middle number
            count = findCount(matrix, mid)
            # or order = sum(bisect.bisect(row, m) for row in matrix) < k:  
            
            if count >= k:
                r = mid # search lower
            else:
                l = mid + 1 # search higher
                
        return l