class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
          
        if len(words1) != len(words2):
            return False
        words = defaultdict(set)
        for word1, word2 in pairs:
            words[word1].add(word2)
            words[word2].add(word1)
        for word1, word2 in zip(words1, words2):
            if word1 != word2 and word2 not in words[word1]:
                return False
        return True