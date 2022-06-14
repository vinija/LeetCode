class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        for i in range(n-1):                                # find index where s[i] < s[i+1], meaning a chance to flip
            if s[i] < s[i+1]: break
        else: return num                                    # if nothing find, return num
        max_idx, max_val = i+1, s[i+1]                      # keep going right, find the maximum value index
        for j in range(i+1, n):
            if max_val <= s[j]: max_idx, max_val = j, s[j]
        left_idx = i                                        # going right from i, find most left value that is less than max_val
        for j in range(i, -1, -1):    
            if s[j] < max_val: left_idx = j
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]   # swap maximum after i and most left less than max
        return int(''.join(s))  