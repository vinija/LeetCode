class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        ans = ''

        for i, word in enumerate(words):
            ans += word[0]

        return ans == s