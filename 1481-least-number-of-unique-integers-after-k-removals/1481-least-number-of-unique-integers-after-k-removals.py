class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mostFreqCounter = Counter(arr).most_common()
        while mostFreqCounter and k >= mostFreqCounter[-1][1]: 
            k -= mostFreqCounter.pop()[1]
        return len(mostFreqCounter)