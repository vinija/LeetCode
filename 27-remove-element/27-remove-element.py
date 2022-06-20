class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for index in range(len(nums)):
            if nums[index] != val:
                nums[count] = nums[index]
                count +=1
        
        return count