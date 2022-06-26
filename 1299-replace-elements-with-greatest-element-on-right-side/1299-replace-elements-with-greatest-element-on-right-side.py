class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue = -1
        for i in range(len(arr)-1, -1, -1):
            maxValue, arr[i] = max(maxValue, arr[i]), maxValue
        return arr  
        