class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr[:] = sorted(arr)
        minDiff = math.inf
        output = []
        
        for index in range(1,len(arr)):
            
            minDiff = min(minDiff,abs(arr[index] - arr[index-1]))
        
        for index in range(1,len(arr)):
            
            if abs(arr[index] - arr[index-1]) == minDiff:
                output.append([arr[index-1],arr[index]])
        
        
        return output
            