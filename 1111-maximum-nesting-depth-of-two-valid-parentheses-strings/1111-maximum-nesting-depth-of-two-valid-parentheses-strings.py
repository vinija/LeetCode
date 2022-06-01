class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = [0]

        for i in range(1,len(seq)):
            if seq[i] == seq[i-1]:
                stack.append(1-stack[i-1])
            else:
                stack.append(stack[i-1])

        return stack
        