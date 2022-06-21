class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        d=collections.Counter(words)
        ans=[]
        d=d.most_common()
        for each in d :
            if k :
                ans.append(each[0])
                k-=1
            else :
                break
        return ans