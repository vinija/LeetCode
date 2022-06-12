class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sortH = sorted(heights)
        
        count = 0
        
        for a, b in zip(sortH,heights):
            if a!= b:
                count +=1
        
        return count