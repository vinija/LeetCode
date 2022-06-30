class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        
        for item in sorted(arr):
            rank.setdefault(item, len(rank)+1)
        
        return map(rank.get,arr)
    
