class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0

        for i, c in enumerate(citations):
            if i < c:
                h_index = i + 1
            else:
                break

        return h_index