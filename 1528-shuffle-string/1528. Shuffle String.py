class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = [''] * len(s)

        for i, index in enumerate(indices):
            r[index] = s[i]
        
        return ''.join(r)
