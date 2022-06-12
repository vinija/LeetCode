class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        
        for index in range(len(numbers)):
            
            if target - numbers[index] not in lookup:
                lookup[numbers[index]] = index
            
            else:
                return [lookup[target-numbers[index]]+1,index+1]