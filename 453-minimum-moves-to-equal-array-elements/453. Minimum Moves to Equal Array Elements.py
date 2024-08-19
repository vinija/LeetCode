class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #Step 1: find the min element in list
        min_num = min(nums)

        #Step 2: calculate the total number of moves needed
        #min # of moves = sum of differences b/w each element and min element
        moves = sum(num - min_num for num in nums)

        #Step 3: return moves
        return moves