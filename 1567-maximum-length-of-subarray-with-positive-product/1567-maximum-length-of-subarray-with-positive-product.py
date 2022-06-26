'''As we traverse through nums, we keep a running size/length of positive and negative products, represented by pos and neg, respectively

The logic is as follows:
if current element is positive then
-positive will be the previous positive length + 1 (because positive x positive = positive)
-negative will be the previous negative length + 1 (because positive x negative = negative and only if a negative product length exists, otherwise its zero)
if current element is negative then
-positive will be the previous negative length + 1 (because negative x negative = positive but only if a neg exists, otherwise its zero)
-negative will be the previous positive length + 1 (because positive x negative = negative)
if current element is zero then
-reset all lengths to zero

The questions is concerned with the maximum length subarray of positive products, so we only use this to update ans.'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
            n = len(nums)
            pos, neg = [0] * n, [0] * n
            if nums[0] > 0: pos[0] = 1
            if nums[0] < 0: neg[0] = 1
            ans = pos[0]
            for i in range(1, n):
                if nums[i] > 0:
                    pos[i] = 1 + pos[i - 1]
                    neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                elif nums[i] < 0:
                    pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                    neg[i] = 1 + pos[i - 1]
                ans = max(ans, pos[i])
            return ans