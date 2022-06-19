from collections import deque
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t = ''.join(s)
        left, right = 0, len(t) - 1
        dq, word = deque(), []
        
        while left <= right:
            if t[left] == ' ' and word:
                dq.appendleft(''.join(word))
                word = []
            elif t[left] != ' ':
                word.append(t[left])
            left += 1
        dq.appendleft(''.join(word))
        
        r = ' '.join(dq)
        for i in range(len(r)):
            s[i] = r[i]