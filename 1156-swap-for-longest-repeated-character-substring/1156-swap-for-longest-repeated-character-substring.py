class Solution:
    def maxRepOpt1(self, text: str) -> int:
        #There are only 2 cases that we need to take care of:
        #extend the group by 1
        #merge 2 adjacent groups together, which are separated by only 1 character
        

        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        listFreq = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(text)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in listFreq)
        # merge 2 groups together
        for i in range(1, len(listFreq) - 1):
            # if both sides have the same char and are separated by only 1 char
            if listFreq[i - 1][0] == listFreq[i + 1][0] and listFreq[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(listFreq[i - 1][1] + listFreq[i + 1][1] + 1, count[listFreq[i + 1][0]]))
        return res
        