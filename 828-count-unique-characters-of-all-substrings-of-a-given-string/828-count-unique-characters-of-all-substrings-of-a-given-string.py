class Solution:
    def uniqueLetterString(self, s: str) -> int:
        last_char_index = defaultdict(int)
        contribution = defaultdict(int)
        res, curr_sum = 0, 0

        for i, c in enumerate(s):
            max_substring_count_at_idx = i + 1
            curr_sum -= contribution[c]
            contribution[c] = max_substring_count_at_idx - last_char_index[c]
            curr_sum += contribution[c]

            res += curr_sum
            last_char_index[c] = i + 1

        return res