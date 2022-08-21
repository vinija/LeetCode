# class Solution:
#     def isScramble(self, s1: str, s2: str) -> bool:
#         if len(s1) != len(s2):
#             return False
#         if s1 == s2:
#             return True
#         if sorted(s1) != sorted(s2): # prunning
#             return False
#         for i in range(1, len(s1)):
#             if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
#             (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
#                 return True
#         return False

# from collections import Counter
# class Solution(object):
#     def isScramble(self, s1, s2):
#         if s1 == s2: return True
#         if Counter(s1) != Counter(s2): return False # early backtracking
#         for i in range(1,len(s1)):
#             if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])): return True
#             if (self.isScramble(s1[:i], s2[-(i):]) and self.isScramble(s1[i:], s2[:-(i)])): return True
#         return False

class Solution(object):
    def __init__(self):
        self.dic = {}

    def isScramble(self, s1, s2):
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
            self.dic[(s1, s2)] = False
            return False
        if s1 == s2:
            self.dic[(s1, s2)] = True
            return True
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
            (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        self.dic[(s1, s2)] = False
        return False    