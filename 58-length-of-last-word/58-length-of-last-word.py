class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s.split())
        return len(s.split().pop())
        