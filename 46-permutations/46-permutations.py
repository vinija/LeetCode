class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

    
        def backtrack(first = 0):
            if first == numsLen:
                output.append(nums[:])
            for index in range(first,numsLen):
                #lets take the integer at index and place it first
                nums[first], nums[index] = nums[index], nums[first]
                
                #backtrack for next integers:
                backtrack(first +1)
                nums[first], nums[index] = nums[index], nums[first]
        
        numsLen = len(nums)
        output = []
        backtrack()
        return output