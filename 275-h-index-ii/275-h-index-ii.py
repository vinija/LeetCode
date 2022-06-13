class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        lens = len(citations)
        
        for index, cite in enumerate(citations):
            if index >= cite:
                return index
        
        return lens
            
