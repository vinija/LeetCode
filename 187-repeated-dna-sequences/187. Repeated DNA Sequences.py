class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        res = set()
        seen = set()

        for i in range(len(s) - 9):
            curr = s[i:i+10]
            if curr in seen:
                res.add(curr)
            seen.add(curr)

        return list(res)