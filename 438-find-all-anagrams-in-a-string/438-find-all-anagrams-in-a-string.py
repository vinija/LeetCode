class Solution:
   def findAnagrams(self, s: str, p: str) -> List[int]:
        needMap, output, pLen, sLen = defaultdict(int), [], len(p), len(s)
        if pLen > sLen: return []

        # build hashmap
        for ch in p: needMap[ch] += 1

        # initial full pass over the window
        for i in range(pLen-1):
            if s[i] in needMap: needMap[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sLen-pLen+1):
            if i > -1 and s[i] in needMap:
                needMap[s[i]] += 1
            if i+pLen < sLen and s[i+pLen] in needMap: 
                needMap[s[i+pLen]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in needMap.values()): 
                output.append(i+1)
                
        return output