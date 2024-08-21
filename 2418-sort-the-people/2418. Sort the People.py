class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        combined = list(zip(heights, names))

        combined.sort(reverse=True, key=lambda x: x[0])

        sorted_names = [name for _, name in combined]

        return sorted_names