class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        currSeq = 1
        maxSeq = 1
        
        for index in range(1,len(nums)):
            if nums[index] != nums[index-1]:
                if nums[index] == nums[index-1]+1:
                    currSeq +=1
                else:
                    
                    maxSeq = max(maxSeq,currSeq)
                    currSeq = 1
        
        return max(maxSeq,currSeq)