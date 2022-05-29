class Solution:
    def isValid(self, s: str) -> bool:  
        opener = '({['
        closer = ')}]'
        stack = []
        for c in s:
            if c in opener:
                stack.append(c)
            else:
                if not stack:
                    return False # No opener at all
                
                last = stack.pop()
                if closer[opener.index(last)] != c: # Not a match
                    return False
        if stack: # Any non-closed parenthesis
            return False
        return True