class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}

        left = 0
        max_len = 0

        for right in range(len(s)):

            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            
            char_index_map[s[right]] = right

            max_len = max(max_len, right - left + 1)
        return max_len