class Solution:
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s == target:
                    return target
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         diff = float('inf')
#         answer = 0
#         length = len(nums)
        
#         nums.sort()
        
#         for index in range(length):
#             low = index + 1
#             high = length -1
            
#             while low < high:
#                 currSum = nums[index] + nums[low] + nums[high]
#                 localDiff = abs(target-currSum)
                
#                 if localDiff == 0:
#                     return currSum
#                 if localDiff < diff:
#                     diff = localDiff
#                     answer = currSum
#                 if currSum < target:
#                     low +=1
#                 else:
#                     high +=1
        
#         return answer