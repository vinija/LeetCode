class Solution:
    def countKeyChanges(self, s: str) -> int:
        key_changes = 0

        for i in range(1, len(s)):
            if s[i].lower() != s[i-1].lower():
                key_changes += 1
        return key_changes