# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         nums.sort()
        
#         currSeq = 1
#         maxSeq = 1
        
#         for index in range(1,len(nums)):
#             if nums[index] != nums[index-1] and nums[index -1] == nums[index]-1:
#                 currSeq +=1
#             else:
#                 currSeq = 1
            
#             maxSeq = max(maxSeq,currSeq)
        
#         return maxSeq
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)