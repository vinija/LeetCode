class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_idx = 0
        stack = []

        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
        return len(stack) == 0