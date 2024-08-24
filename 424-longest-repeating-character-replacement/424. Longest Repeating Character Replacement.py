from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        max_length = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            # Add the current character to the frequency count
            char_count[s[right]] += 1
            
            # Update the max_count with the highest frequency in the current window
            max_count = max(max_count, char_count[s[right]])
            
            # Current window size is right - left + 1
            # Check if the window is valid by ensuring the number of replacements needed <= k
            while (right - left + 1) - max_count > k:
                # Window is not valid, shrink the window from the left
                char_count[s[left]] -= 1
                left += 1
            
            # Update the maximum length of valid window
            max_length = max(max_length, right - left + 1)

        return max_length
