class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        out = [-1]
        greatest = 0
        for num in arr[::-1]:
            if greatest < num:
                greatest = num
            out.append(greatest)
        out.pop()
        return out[::-1]