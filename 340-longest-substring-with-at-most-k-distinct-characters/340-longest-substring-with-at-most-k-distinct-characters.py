class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen_letters = {}
        max_len = left = 0
        
        for right in range(len(s)):
            if s[right] not in seen_letters:
                seen_letters[s[right]] = 0
            seen_letters[s[right]] += 1
            while len(seen_letters) > k:
                seen_letters[s[left]] -= 1
                if seen_letters[s[left]] == 0:
                    del seen_letters[s[left]]
                left += 1


            max_len = max(max_len, right-left+1)
        
        return max_len
