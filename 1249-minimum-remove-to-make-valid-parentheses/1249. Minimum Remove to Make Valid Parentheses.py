from typing import List, Set, Optional

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #stack to keep track of indices of (
        stack = []

        #set to keep track of indices to remove
        to_remove = set()

        #first pass to find indices of invalid parens
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        #if anything left in stack, add to be removed
        to_remove = to_remove.union(set(stack))

        #second pass to create the valid string
        result = []
        
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)
        
        return ''.join(result)

        