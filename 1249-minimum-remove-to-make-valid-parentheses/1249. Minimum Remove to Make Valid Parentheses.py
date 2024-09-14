class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Keep track of the indices of invalid parens
        invalid_indicies = set()
        stack = []

        #Identify invalid parens
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    invalid_indicies.add(i)

        #add to set
        invalid_indicies.update(stack)

        #return
        return "".join([char for i, char in enumerate(s) if i not in invalid_indicies])