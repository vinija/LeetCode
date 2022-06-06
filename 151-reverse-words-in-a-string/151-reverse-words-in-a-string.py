from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) -1
        
        while left <= right and s[left] == " ":
            left +=1
        
        
        while left <= right and s[right] == " ":
            right -=1
        
        localDeque, word = deque(), []
        
        while left <= right:
            if s[left] == " " and word:
                localDeque.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left +=1
        localDeque.appendleft("".join(word))
        return " ".join(localDeque)
        
            