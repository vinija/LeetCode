
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        wordDict = set(wordDict)
        def dfs(subpath, string):
            if string == "":
                ans.append(" ".join(subpath))
                return
            
            for word in wordDict:
                if string.startswith(word):
                    subpath.append(word)
                    dfs(subpath, string[len(word):])
                    subpath.pop()
            
        dfs([], s)
        return ans