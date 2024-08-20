class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0

        for row in matrix:
            for value in row:
                total_sum += abs(value)

                if value < 0:
                    negative_count += 1
                
                min_abs_value = min(min_abs_value, abs(value))
        
        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs_value