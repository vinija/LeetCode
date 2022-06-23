class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

            wordDict = set(wordDict)

            sentences = []

            def recurse(ind, string):

                if ind == len(s):

                    sentences.append(string[:-1])

                for i in range(ind,len(s)+1):

                    if s[ind:i] in wordDict:

                        recurse(i, string+s[ind:i]+" ")

            recurse(0,"")

            return sentences