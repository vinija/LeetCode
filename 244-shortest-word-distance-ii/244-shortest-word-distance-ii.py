class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = defaultdict(list)
        
        for index, word in enumerate(wordsDict):
            self.dict[word].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:
        minDist = math.inf
        word1Index = self.dict[word1]
        word2Index = self.dict[word2]
        
        for first in word1Index:
            for second in word2Index:
                minDist = min(minDist, abs(first-second))
        
        return minDist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)