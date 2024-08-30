class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {char: 0 for char in s}

        for c in s:
            freq[c] += 1
        
        stack = []
        visited = set()

        for char in s:

            freq[char] -= 1

            #check if in visited already
            if char in visited:
                continue
            
            #process the removal
            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                removed_char = stack.pop()
                visited.remove(removed_char)
            
            stack.append(char)
            visited.add(char)
        return ''.join(stack)

            #add the current character to the stack