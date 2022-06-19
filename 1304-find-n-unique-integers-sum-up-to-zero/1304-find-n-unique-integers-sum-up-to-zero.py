class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        output = []
        for index in range(1,n//2 + 1):
            output.append(index*-1)
            output.append(index)
        
        if len(output) != n:
            output.append(0)
        
        return output