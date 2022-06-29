class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = defaultdict(str)
        
        for index, char in enumerate(s):
            if char not in hashmap:
                if t[index] in hashmap.values():
                    return False
                else:
                    hashmap[char] = t[index]
            else:
                if hashmap[char] != t[index]:
                    return False
        
        return True