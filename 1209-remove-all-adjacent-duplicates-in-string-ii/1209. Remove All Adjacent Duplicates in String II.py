class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Stack to store tuples of (character, frequency)
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                # If the top of the stack is the same character, increment the count
                stack[-1] = (char, stack[-1][1] + 1)
                # If the count reaches k, pop the element from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Otherwise, push the character and a count of 1
                stack.append((char, 1))
        
        # Rebuild the final string from the stack
        result = []
        for char, count in stack:
            result.append(char * count)
        
        return ''.join(result)
