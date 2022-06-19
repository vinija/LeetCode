class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [""] * (len(s))
        
        for a,b in zip(s,indices):
            output[b] = a
        
        return "".join(output)