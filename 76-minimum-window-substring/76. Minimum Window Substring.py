class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)            # hash table to store char frequency
        missing = len(t)                         # total number of chars we care
        start, end = 0, 0 
        i = 0 
        for j, char in enumerate(s, 1):          # index j from 1
            if need[char] > 0:                   # or simply "missing -= need[c] > 0"
                missing -= 1 
            need[char] -= 1 
            if not missing:                      # match all chars
                while i < j and need[s[i]] < 0:  # remove chars to find the real start
                    need[s[i]] += 1 
                    i += 1 
                need[s[i]] += 1                  # make sure the first appearing char satisfies need[char]>0
                missing += 1                     # we missed this first char, so add missing by 1
                if not end or j-i < end-start:   # update window
                    start, end = i, j 
                i += 1                           # update i to start+1 for next window
        return s[start:end]