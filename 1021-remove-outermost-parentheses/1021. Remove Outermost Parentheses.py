class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0

        for char in s:
            if char == '(':
                if opened > 0:
                    result.append(char)
                opened += 1
            elif char == ')':
                opened -= 1
                if opened > 0:
                    result.append(char)
        return ''.join(result)
        