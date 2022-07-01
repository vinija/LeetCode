class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        sumsVisitedSoFar = set([0])
        curSum, prevSum = 0, 0
        for i,n in enumerate(nums):
            curSum += n
            curSum = curSum % k
            if i!=0 and curSum in sumsVisitedSoFar:
                return True
            
            sumsVisitedSoFar.add(prevSum)
            prevSum = curSum
        
        return False