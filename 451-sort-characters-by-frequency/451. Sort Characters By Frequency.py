from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_chars = sorted(freq.keys(), key = lambda x: (-freq[x], x))

        result = ''.join([char * freq[char] for char in sorted_chars])

        return result

        