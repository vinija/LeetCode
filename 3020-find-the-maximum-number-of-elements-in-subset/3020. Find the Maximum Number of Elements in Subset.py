class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans, freqMap = 0, Counter(nums)
        for val, freq in sorted(freqMap.items()):
            temp, maxLen = val, 0
            while temp in freqMap and freqMap[temp] > 0:
                # case when only n no of 1s are present 
                if temp == 1: maxLen += freqMap[temp]
                elif freqMap[temp] >= 2: maxLen += 2
                # when frequency is only 1 then we cannot proceed further in the sequence
                else: maxLen += 1; break
                # set to zero iterated key value, so that 
                # we don't check this sequence in future
                freqMap[temp] = 0
                # break when the next square is out of interger range
                if temp > 1000000000: break
                temp *= temp
            # When the sequence broken with the point where the 
            # largest number has more than or equal to 2 occurance 
            # but we can take only one
            if not maxLen % 2: maxLen -= 1
            ans = max(ans, maxLen)
        return ans
        