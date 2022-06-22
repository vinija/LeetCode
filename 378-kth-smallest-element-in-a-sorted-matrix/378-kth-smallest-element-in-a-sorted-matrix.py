class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        output = []
        #heapq.heapify(matrix)
        for mat in matrix:
            for val in mat:
                output.append(val)
        output[:] = sorted(output)
        return output[k-1]